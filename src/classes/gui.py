"""Classes for use in the gui version"""

# Builtins
import random
import requests
from typing import Tuple

# My functions
from PyQt5 import QtWidgets
from src.helpers import *
# For type hints
from src.classes.input import *
from src.classes.calculator import Calculator
from src.classes.weather import Weather

# Generated gui
try:
    from src.GUIs import qt_v2, settings_v2
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
        self.server_url, self.server_port = server_info
        self.server_uid = server_uid
        self.internet = False

        # Start internet checker
        self.internet_thread = threading.Thread(target=self.__update_connection)
        self.internet_thread.start()

        # Hook buttons
        self.enter_button.clicked.connect(self.__sort_input)
        self.settings_button.clicked.connect(self.__open_settings)

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

            if resp.status_code == 200:
                data = resp.json()
                if data["n"] == 0:
                    self.add_to_output("No new messages")
                else:
                    self.add_to_output(
                        "Your unread messages:\n" + "\n".join(data["data"])
                    )
            else:
                logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")

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

    def __add_welcome(self):
        text = self.text_entry.text()
        with open(self.settings_path+"\\messages.json", "r") as f:
            messages = json.load(f)
        messages["welcome"].append(text)
        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(messages, f)

    def __add_no_ans(self):
        text = self.text_entry.text()
        with open(self.settings_path+"\\messages.json", "r") as f:
            messages = json.load(f)
        messages["no answer"].append(text)
        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(messages, f)

    def __add_trans(self):
        old, new = self.text_entry.text().split(":")
        with open(self.settings_path+"\\translations.json", "r") as f:
            translations = json.load(f)

        translations["data"][old] = new

        with open(self.settings_path+"\\messages.json", "w") as f:
            json.dump(translations, f)

    def __add_channel(self):
        id_ = self.text_entry_2.text()
        resp = requests.post(
            f"http://{self.server_url}:{self.server_port}/add_channel",
            {"u": self.server_uid, "c": str(id_)}
        )

        if resp.status_code != 200:
            logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")

    def __remove_channel(self):
        id_ = self.text_entry_2.text()
        resp = requests.post(
            f"http://{self.server_url}:{self.server_port}/remove_channel",
            {"u": self.server_uid, "c": str(id_)}
        )

        if resp.status_code != 200:
            logError("Discord Integration", "Non-200 response", f"Server responded with: {resp.text}")
