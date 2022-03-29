"""Base class for the scripting functionality"""


# My functions
import re
from ..helpers import *

# Builtins
import json
from PyQt5.QtWidgets import QMessageBox

# Not-Builtin
try:
    import requests
except ImportError as e:
    logException("Scripting", e)
    print("Uninstalled package, try `pip install requests`")
    quit()


class Scripting:
    def __init__(self, storage_path: str):
        logInfo("Scripting", "Scripting started")
        self.path = storage_path
        with open(storage_path + "\\scripts.json") as f:
            self.scripts: dict = json.load(f)

    def exec_script(self, name: str, input_: str, output: callable, internet: bool):
        """Execute a Script
        
        :param name: Name of the script to execute
        :param input_: Input to provide to the Script
        :param output: The function to add to output
        :param internet: Whether a connection to the internet exists
        """

        if name in self.scripts:
            output(f"Running script {name}")
            for action in self.scripts[name]["actions"]:
                if action["type"] == "Response":
                    output(action["response"])
                elif action["type"] == "Format":
                    input_ = re.findall(action["pattern"], input_)[0]
                elif action["type"] == "HTML Request":
                    if internet:
                        resp = requests.get(input_ if action["use input"] else action["url"])
                        with open(f"{self.path}\\{name}.html", "w") as f:
                            f.write(resp.text)
                        output(f"Script {name} outputted to {self.path}\\{name}.html")
                    else:
                        QMessageBox(
                            QMessageBox.Icon.Critical,
                            "Script Failed",
                            f"Cannot run Script {name} with no internet"
                        ).exec()
                elif action["type"] == "JSON Request":
                    if internet:
                        resp = requests.get(input_ if action["use input"] else action["url"])
                        output(json.dumps(resp.json(), indent=2))
                    else:
                        QMessageBox(
                            QMessageBox.Icon.Critical,
                            "Script Failed",
                            f"Cannot run Script {name} with no internet"
                        ).exec()
