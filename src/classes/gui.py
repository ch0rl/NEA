"""Classes for use in the gui version"""

# Builtins
import re
import random
import requests
from typing import Tuple

# My functions
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from src.helpers import *
# For type hints
from src.classes.input import *
from src.classes.calculator import Calculator
from src.classes.weather import Weather
from src.classes.scripting import Scripting

# Generated gui
try:
    from src.GUIs import qt_v2, settings_v2, scripting_v1
except ImportError as e:
    logException("GUI Classes", e)
    print("No GUI template file found")
    quit()


class Main_GUI(QtWidgets.QMainWindow, qt_v2.Ui_MainWindow):
    """Main GUI class, using the pre-generated ui"""

    def __init__(self,
                 welcome_message: str,
                 text_input_handler: Text_Input_Handler,
                 speech_input_handler: Speech_Input_Handler,
                 calc: Calculator,
                 weather: Weather,
                 messages: list,
                 scripting: Scripting,
                 server_info: Tuple[str, int],
                 server_uid: str,
                 *args, **kwargs
                 ):
        """Main GUI class

        :param welcome_message: Message to be displayed
        :param text_input_handler: Input handler in use
        :param speech_input_handler: Speech handler in use
        :param calc: Calculator object in use
        :param weather: Weather object in use
        :param messages: Messages in use
        :param scripting: Scripting in use
        :param server_info: Access information for the server, in form
            (url, port)
        :param server_uid: `User id` when communicating with the server
        :param *args, **kwargs: Any args to pass to super
        """
        # Sort pre-generated UI
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Sort objects
        self.text_input_handler = text_input_handler
        self.speech_input_handler = speech_input_handler
        self.calc = calc
        self.weather = weather
        self.messages = messages
        self.scripting = scripting
        self.server_url, self.server_port = server_info
        self.server_uid = server_uid
        self.internet = False

        # Start internet checker
        self.internet_thread = threading.Thread(target=self.__update_connection)
        self.internet_thread.start()

        # Hook buttons
        self.enter_button.clicked.connect(self.__sort_input)
        self.settings_button.clicked.connect(self.__open_settings)
        self.scripting_button.clicked.connect(self.__open_scripts)

        # Add welcome message
        self.welcome_message.setText(welcome_message)
        self.output_text.setText("Output: \n")

    def __open_settings(self):
        self.settings_win = Settings_GUI(
            "settings",
            (self.server_url, self.server_port),
            self.server_uid
        )
        self.settings_win.show()

    def __open_scripts(self):
        self.scripting_win = Scripting_GUI(
            self.scripting.path
        )
        self.scripting_win.show()

    def __update_connection(self):
        while True:
            try:
                requests.get("http://example.com")
            except requests.ConnectionError:
                self.internet = False
            else:
                self.internet = True
            time.sleep(1)

    def __sort_input(self):
        """Handles any input"""
        text = self.text_entry.text()
        self.text_entry.setText("")
        input_ = self.text_input_handler.parse_raw_text(text)
        command, data = input_["command"], input_["data"]

        if command == "speech":
            self.add_to_output("Listening for audio")
            audio = self.speech_input_handler.listen(10)
            if audio is not None:
                input_ = self.speech_input_handler.parse_raw_audio(audio, not self.internet)
                if input_ is not None:
                    command, data = input_["command"], input_["data"]
                else:
                    self.add_to_output(random.choice(self.messages["no answer"]))
                    return
            else:
                command, data = "", "Audio Not Recognized"

        if command == "calculator":
            self.add_to_output(f"\nYou said: 'Calculate {data}'")
            # Parse expression
            ans = self.calc.parse(data)

            if ans is not None:
                self.add_to_output(f"Answer: {ans}")
            else:
                self.add_to_output(random.choice(self.messages["no answer"]))

            # Newline
            self.add_to_output()

        elif command == "weather":
            self.add_to_output(
                f"You said: 'What is the weather like at/in {data}'")
            # Fetch weather
            response = self.weather.weather(data)

            # If weather is returned
            if response is not None:
                self.add_to_output(response)
            else:
                self.add_to_output(random.choice(self.messages["no answer"]))

            # Newline
            self.add_to_output()

        elif command == "discord":
            self.add_to_output(f"You said: Read my discord messages (user: {self.server_uid})")
            resp = requests.get(
                f"http://{self.server_url}:{self.server_port}/get_messages",
                {"u": self.server_uid}
            )

            if resp.status_code // 100 != 2:
                data = resp.json()
                if data["n"] == 0:
                    self.add_to_output("No new messages")
                else:
                    self.add_to_output(
                        "Your unread messages:\n" + "\n".join(data["data"])
                    )
            else:
                logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")
                QMessageBox(
                    QMessageBox.Icon.Icon.Critical,
                    "Server Error",
                    "Server responded with a non-200 response, see errors for more information"
                ).exec()
        else:
            # If all else fails, try scripts
            with open(f"{self.scripting.path}\\scripts.json") as f:
                scripts = json.load(f)
            
            for name, script in scripts.items():
                if script["trigger"] in text:
                    self.scripting.exec_script(
                        name, text,
                        self.add_to_output,
                        self.internet
                    )
                    break
            else:
                if data == "Audio Not Recognized":
                    self.add_to_output(data)
                else:
                    self.add_to_output(f"You said: {data}")
                    self.add_to_output(random.choice(self.messages["no answer"]))

    def add_to_output(self, text: str = None):
        """Adds `text` to the output label, with the time and a newline

        :param text: Text to add
        """

        if text:
            self.output_text.append(f"[{time.strftime(TIME_FMT)}] {text}\n")
        else:
            self.output_text.append("\n")


class Settings_GUI(QtWidgets.QWidget, settings_v2.Ui_Form):
    """Settings UI, using pre-generated code"""

    def __init__(self,
                 settings_path: str,
                 server_info: Tuple[str, int],
                 server_uid: str,
                 *args, **kwargs
                 ):
        """Settings UI

        :param settings_path: Path to the settings directory
        :param server_info: Access information for the server, in form
            (url, port)
        :param server_uid: `User id` when communicating with the server
        :param *args, **kwargs: Any args to pass to super
        """
        # Sort pre-generated UI
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.settings_path = settings_path
        self.server_url, self.server_port = server_info
        self.server_uid = server_uid

        # Hook buttons
        self.welc_button.clicked.connect(self.__add_welcome)
        self.no_ans_button.clicked.connect(self.__add_no_ans)
        self.trans_button.clicked.connect(self.__add_trans)

        self.add_c_button.clicked.connect(self.__add_channel)
        self.remove_c_button.clicked.connect(self.__remove_channel)

        self.sync_trans_append.clicked.connect(lambda: self.__update_translations("a"))
        self.sync_trans_owrite.clicked.connect(lambda: self.__update_translations("w"))

    def __add_welcome(self):
        text = self.text_entry.text()
        with open(self.settings_path+"\\messages.json", "r") as f:
            messages = json.load(f)
        messages["welcome"].append(text)
        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(messages, f)
        QMessageBox(
            QMessageBox.Icon.Information, "",
            f"Added {text} to welcome messages"
        ).exec()

    def __add_no_ans(self):
        text = self.text_entry.text()
        with open(self.settings_path+"\\messages.json", "r") as f:
            messages = json.load(f)
        messages["no answer"].append(text)
        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(messages, f)
        QMessageBox(
            QMessageBox.Icon.Information, "",
            f"Added {text} to no answer messages"
        ).exec()

    def __add_trans(self):
        old, new = self.text_entry.text().split(":")
        with open(self.settings_path+"\\translations.json", "r") as f:
            translations = json.load(f)

        translations["data"][old] = new

        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(translations, f)
        QMessageBox(
            QMessageBox.Icon.Information, "",
            f"Added {old} -> {new} to translations"
        ).exec()

    def __add_channel(self):
        id_ = self.text_entry_2.text()
        resp = requests.post(
            f"http://{self.server_url}:{self.server_port}/add_channel",
            {"u": self.server_uid, "c": str(id_)}
        )

        if resp.status_code // 100 != 2:
            logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")
            QMessageBox(
                QMessageBox.Icon.Critical,
                "Server Error",
                "Server responded with a non-200 response, see errors for more information"
            ).exec()
        else:
            QMessageBox(
                QMessageBox.Icon.Information, "",
                f"Added {id_} to channels"
            ).exec()

    def __remove_channel(self):
        id_ = self.text_entry_2.text()
        resp = requests.post(
            f"http://{self.server_url}:{self.server_port}/remove_channel",
            {"u": self.server_uid, "c": str(id_)}
        )

        if resp.status_code // 100 != 2:
            logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")
            QMessageBox(
                QMessageBox.Icon.Critical,
                "Server Error",
                "Server responded with a non-200 response, see errors for more information"
            ).exec()
        else:
            QMessageBox(
                QMessageBox.Icon.Information, "",
                f"Removed {id_} from channels"
            ).exec()
    
    def __update_translations(self, mode: str):
        with open(self.settings_path+"\\translations.json") as f:
            translations = json.load(f)
        ver = translations["version"]

        resp = requests.get(
            f"http://{self.server_url}:{self.server_port}/sync_rules",
            {"v": str(ver)}
        )

        if resp.status_code // 100 != 2:
            logError("Translation Sync", "Non-200 response", f"Server responded with: {resp.text}")
            QMessageBox(
                QMessageBox.Icon.Warning,
                "Server Error",
                "Server responded with a non-200 response, see logs for more information"
            ).exec()
        elif resp.status_code == 204:
            # Already up-to-date
            QMessageBox(
                QMessageBox.Icon.Information,
                "Already up-to-date",
                f"You already have the most up-to-date translations (version: {ver})"
            ).exec()
        else:
            new_translations = resp.json()
            if mode == "w":
                with open(self.settings_path+"\\translations.json", "w") as f:
                    json.dump(new_translations, f)
            else:
                for k in ("command", "data", "speech specific"):
                    for k_, v in new_translations[k].items():
                        if (
                                k_ in translations[k] and
                                type(translations[k][k_]) == list
                            ):
                            translations[k][k_].extend(
                                [i for i in v if i not in translations[k][k_]]
                            )
                        elif k_ not in translations[k]:
                            translations[k][k_] = v
                            
                with open(self.settings_path+"\\translations.json", "w") as f:
                    json.dump(translations, f)
            QMessageBox(
                QMessageBox.Icon.Information,
                "Updated translations",
                f"Translations are now up-to-date (version: {ver})"
            ).exec()


class Scripting_GUI(QtWidgets.QWidget, scripting_v1.Ui_Scripting_UI):
    """Scripting UI, using pre-generated code"""

    def __init__(self, storage_path: str, *args, **kwargs):
        """Scripting UI

        :param storage_path: Path to the scripting storage
        :param *args, **kwargs: Any args to pass to super
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.path = storage_path
        self.name = ""
        self.script = None
        with open(f"{self.path}\\scripts.json") as f:
            self.scripts = json.load(f)
        self.additional_types = {
            "Response": lambda x: {"response": x},
            "Format": lambda x: {"pattern": re.compile(x)},
            "HTML Request": lambda x: {
                "use input": x.lower() == "use input",
                "url": x if not x.lower() == "use input" else None
            },
            "JSON Request": lambda x: {
                "use input": x.lower() == "use input",
                "url": x if not x.lower() == "use input" else None
            }
        }

        # Hook buttons
        self.select_script.clicked.connect(self.__select_script)
        self.add_action.clicked.connect(self.__add_action)
    
    def __select_script(self):
        name = self.name_entry.text()
        if name:
            self.script = name
            self.label.setText(f"Scripting - {name}")
            self.name_entry.setText("")

            with open(f"{self.path}\\scripts.json") as f:
                self.scripts = json.load(f)
            
            if name not in self.scripts:
                self.scripts[name] = {
                    "actions": []
                }
        else:
            QMessageBox(
                QMessageBox.Icon.Warning,
                "Name Required",
                "A name of a script is required"
            ).exec()

    def __add_action(self):
        trigger = self.trigger_entry.text()
        self.trigger_entry.setText("")
        action = self.action_entry.currentText()
        additional = self.additional_entry.text()
        self.additional_entry.setText("")

        if self.script:
            if action and additional:
                if trigger:
                    self.scripts[self.script]["trigger"] = trigger
                
                self.scripts[self.script]["actions"].append({
                    "type": action,
                    **self.additional_types[action](additional)
                })

                with open(f"{self.path}\\scripts.json", "w") as f:
                    json.dump(self.scripts, f)
            else:
                QMessageBox(
                    QMessageBox.Icon.Warning,
                    "Item missing",
                    "Both action and additional require a value"
                ).exec()
        else:
            QMessageBox(
                QMessageBox.Icon.Warning,
                "Missing script",
                "A script is needed to be selected first"
            ).exec()
