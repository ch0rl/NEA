"""Main run file for the cli version"""


# My functions
import requests
from .classes.calculator import Calculator
from .classes.weather import Weather
from .helpers import logInfo

# Builtins
import random
import json

# Start
logInfo("Main", "CLI Started")

# Setup objects
calc = Calculator()
weather = Weather()

# Get lists of messages
with open("settings/messages.json", 'r') as f:
    MESSAGES = json.load(f)

# Welcome user
print(random.choice(MESSAGES["welcome"]))

running = True
while running:
    # Keep going until they stop
    command = input("Command > ").lower()

    if command == "quit":
        running = False
        
    elif command == "calculator":
        expression = input("Expression > ").lower()
        print(f"\nYou said: 'Calculate {expression}'")
        # Parse expression
        ans = calc.parse(expression)

        # If ans isn't None
        if ans is not None:
            print(f"Answer: {ans}")
        else:
            print(random.choice(MESSAGES["no answer"]))
        
        # Newline
        print()

    elif command == "weather":
        location = input("Location: ").lower()
        print(f"You said: 'What is the weather like at/in {location}'")
        # Fetch weather
        response = weather.weather(location)

        # If weather is returned
        if weather is not None:
            print(response)
        else:
            print(random.choice(MESSAGES["no answer"]))
        
        # Newline
        print()

logInfo("Main", "Program stopping")
