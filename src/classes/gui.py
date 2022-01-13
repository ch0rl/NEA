"""Classes for use in the gui version"""

# Builtins
import random

# My functions
from PyQt5 import QtWidgets
import speech_recognition
from src.helpers import *
# For type hints
from src.classes.input import *
from src.classes.calculator import Calculator
from src.classes.weather import Weather

# Generated gui
try:
    from src.GUIs import qt_v2, settings_v1
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
            *args, **kwargs
        ):
        """Main GUI class
        
        :param welcome_message: Message to be displayed
        :param text_input_handler: Input handler in use
        :param speech_input_handler: Speech handler in use
        :param calc: Calculator object in use
        :param weather: Weather object in use
        :param messages: Messages in use
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

        # Hook buttons
        self.enter_button.clicked.connect(self.__sort_input)
        self.settings_button.clicked.connect(self.__open_settings)

        # Add welcome message
        self.welcome_message.setText(welcome_message)
        self.output_text.setText("Output: \n")

    def __open_settings(self):
        self.settings_win = Settings_GUI("settings")
        self.settings_win.show()


    def __sort_input(self):
        """Handles any input"""
        text = self.text_entry.text()
        self.text_entry.setText("")
        input_ = self.text_input_handler.parse_raw_text(text)
        command, data = input_["command"], input_["data"]

        # Logic from cli.py
        if command == "speech":
            input_ = self.speech_input_handler.get_input()
            command, data = input_["command"], input_["data"]

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


class Settings_GUI(QtWidgets.QWidget, settings_v1.Ui_Settings_win):
    """Settings UI, using pre-generated code"""
    def __init__(self,
            settings_path: str,
            *args, **kwargs
        ):
        """Settings UI
        
        :param settings_path: Path to the settings directory
        :param *args, **kwargs: Any args to pass to super
        """
        # Sort pre-generated UI
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.settings_path = settings_path

        # Hook buttons
        self.welc_button.clicked.connect(self.__add_welcome)
        self.no_ans_button.clicked.connect(self.__add_no_ans)
        self.trans_button.clicked.connect(self.__add_trans)

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
