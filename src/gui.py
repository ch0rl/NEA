"""Main run file for the gui version"""


# My functions
from .classes.input import *
from .classes.gui import *
from .classes.calculator import Calculator
from .classes.weather import Weather
from .helpers import *

# Builtins
import random
import json

# Not builtin
try:
    import PyQt5.QtWidgets as Qwidgets
except ImportError as e:
    logException("Speech Input", e)
    print("Uninstalled package, try `pip install pyqt5`")
    quit()

# Start
logInfo("Main", "GUI Started")

# Setup objects
calc = Calculator()
weather = Weather()
text_input = Text_Input_Handler()
speech_input = Speech_Input_Handler()

# Get lists of messages
with open("settings/messages.json", 'r') as f:
    MESSAGES = json.load(f)

# Get server info
with open("settings/server.json", "r") as f:
    SERVER_INFO = json.load(f)

# Setup application
APP = Qwidgets.QApplication([])
MAIN_GUI = Main_GUI(
    random.choice(MESSAGES["welcome"]),
    text_input, speech_input, calc, weather, MESSAGES,
    (SERVER_INFO["url"], SERVER_INFO["port"]),
    SERVER_INFO["uid"]
)
MAIN_GUI.show()
APP.exec()
