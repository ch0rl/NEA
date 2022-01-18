"""Main run file for the cli version"""


# My functions
from src.classes.input import *
from .classes.calculator import Calculator
from .classes.weather import Weather
from .helpers import *

# Builtins
import random
import json

# Start
logInfo("Main", "CLI Started")

# Setup objects
calc = Calculator()
weather = Weather()
text_input = Text_Input_Handler()
speech_input = Speech_Input_Handler()
kb_handler = Keyboard_Handler()
kb_handler.start_thread()

# Get lists of messages
with open("settings/messages.json", 'r') as f:
    MESSAGES = json.load(f)

# Welcome user
print(random.choice(MESSAGES["welcome"]))

running = True
while running:
    # Sort input
    if kb_handler.newline:
        input_ = text_input.get_input(kb_handler)
        command, data = input_["command"], input_["data"]

        # TODO: Improve
        if command == "speech":
            input_ = speech_input.get_input()
            print(f"You said: {input_}")
            command, data = input_["command"], input_["data"]

        if command == "calculator":
            print(f"\nYou said: 'Calculate {data}'")
            # Parse expression
            ans = calc.parse(data)

            # If ans isn't None
            if ans is not None:
                print(f"Answer: {ans}")
            else:
                print(random.choice(MESSAGES["no answer"]))

            # Newline
            print()

        elif command == "weather":
            print(f"You said: 'What is the weather like at/in {data}'")
            # Fetch weather
            response = weather.weather(data)

            # If weather is returned
            if weather is not None:
                print(response)
            else:
                print(random.choice(MESSAGES["no answer"]))

            # Newline
            print()

        else:
            print(random.choice(MESSAGES["no answer"]))

logInfo("Main", "Program stopping")
