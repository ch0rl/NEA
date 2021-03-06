"""Base class for the calculator functionality"""


# My functions
from ..helpers import *
from .structures import Stack
from PyQt5.QtWidgets import QMessageBox

# Builtins
import re
import json

# Not builtin
try:
    import requests
    import urllib.parse as parse
except ImportError as e:
    logException("Calculator", e)
    print("Uninstalled package, try `pip install requests`")
    quit()


class Calculator:
    OPERATORS = ["+", "-", "*", "/"]
    # PRECEDENCES used in evaluation
    PRECEDENCES = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0, ")": 0}
    # Allowed chars (regex format)
    CHARS = r"+-\/\*\()\."
    # To avoid quitting on math errors
    ERROR = ArithmeticError

    def __init__(self):
        logInfo("Calculator", "Calculator started")
        self.last_output: str = None

    @staticmethod
    def validate(expression: str) -> bool:
        """Validates whether `expression` is likely a numerical expression
        
        :param expression: The expression to validate
        :return: Whether it is likely a numerical expression
        """

        # Check for numbers and allowed chars
        return bool(re.match(fr"^[0-9{Calculator.CHARS}\s]+$", expression))

    def parse(self, expression: str, internet: bool = False) -> str:
        """Parse an expression
        
        :param expression: The expression itself
        :param internet: Whether or not a connection to the internet exists
        :return: Result of expression, None if not calculable
        """

        expression = expression.replace(" ", "")
        # Basic validation
        if self.validate(expression):
            values = Stack()
            ops = Stack()
            i = 0

            # Loop over expression
            while i < len(expression):
                token = expression[i]
                if token == "(":
                    # Start of 'sub-expression'
                    ops.push(token)
                elif token == ")":
                    # End of 'sub-expression'
                    while len(ops) and ops.peek() != "(":
                        val2, val1 = values.pop(), values.pop()
                        op = ops.pop()

                        try:
                            values.push(eval(f"{val1} {op} {val2}"))
                        except ArithmeticError as e:
                            logException("Calculator", e)
                            QMessageBox(
                                QMessageBox.Icon.Critical,
                                "Math Error",
                                f"Cannot parse '{val1} {op} {val2}' due to a math error"
                            ).exec()
                            return None
                    ops.pop()
                elif token.isnumeric():
                    # Make base-10 number in string
                    val = 0
                    while i < len(expression) and expression[i].isnumeric():
                        val = val * 10 + int(expression[i])
                        i += 1
                    values.push(val)
                    i -= 1
                else:
                    # An operator
                    while len(ops) and Calculator.PRECEDENCES[ops.peek()] > Calculator.PRECEDENCES[token]:
                        val2, val1 = values.pop(), values.pop()
                        op = ops.pop()
                        try:
                            values.push(eval(f"{val1} {op} {val2}"))
                        except ArithmeticError as e:
                            logException("Calculator", e)
                            QMessageBox(
                                QMessageBox.Icon.Critical,
                                "Math Error",
                                f"Cannot parse '{val1} {op} {val2}' due to a math error"
                            ).exec()
                            return None
                    ops.push(token)
                i += 1
            
            # Finish up
            while len(ops):
                val2, val1 = values.pop(), values.pop()
                op = ops.pop()

                try:
                    values.push(eval(f"{val1} {op} {val2}"))
                except ArithmeticError as e:
                    logException("Calculator", e)
                    QMessageBox(
                        QMessageBox.Icon.Critical,
                        "Math Error",
                        f"Cannot parse '{val1} {op} {val2}' due to a math error"
                    ).exec()
                    return None
            
            ans = str(values.pop())
            self.last_output = ans
            return ans

        elif internet:
            # Not validated so try Wolfram Alpha
            with open("settings/api-keys.json", 'r') as f:
                try:
                    key = json.load(f)["Wolfram|Alpha"]
                except KeyError as e:
                    key = None
                    logException("Calculator", e)
            
            # Have to have API key for this to work
            if key:
                urlEncoded = parse.quote(expression, safe="")
                resp = requests.get(
                    f"http://api.wolframalpha.com/v1/result?appid={key}&i={urlEncoded}"
                )
                if resp.status_code == 200:
                    # 200 = All good
                    logInfo("Calculator", "Wolfram|Alpha used")
                    ans = resp.text
                    self.last_output = ans
                    return ans
                    
                else:
                    # Bad status code
                    logError("Calculator", "Bad API return", "Wolfram|Alpha API returned a non-200 status code")
                    return None
        else:
            logError("Calculator", "Failed to answer", f"Unable to parse expression: {expression} and not connected to the internet")
