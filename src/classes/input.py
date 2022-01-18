"""Base class for speech recognition and translation"""

# My functions
from ..helpers import *

# Builtin
import json
import threading
from collections import defaultdict

# Not builtin
try:
    import speech_recognition as sr
except ImportError as e:
    logException("Speech Input", e)
    print("Uninstalled package, try `pip install SpeechRecognition`")
    quit()


class Keyboard_Handler:
    """Class for handling the keyboard in the background"""
    def __init__(self):
        logInfo("Keyboard Handler", "Keyboard Handler started")
        self.buffer = ""
        self.newline = False

    def __watch_keyboard(self):
        while True:
            text = input()

            self.buffer += text
            self.newline = True

    def start_thread(self) -> None:
        """Starts the background thread for watching the keyboard"""
        self.thread = threading.Thread(target=self.__watch_keyboard)
        self.thread.start()

    def access_text(self, delete: bool = True) -> str:
        """Return the text saved in the buffer
        
        :param delete: Whether to clear the buffer or not
        :return: The text saved in the buffer
        """

        string = self.buffer
        self.newline = False

        if delete:
            self.buffer = ""
        
        return string


class Text_Input_Handler:
    """Class for handling text input"""
    def __init__(self):
        logInfo("Text Input", "Text Input started")

        with open("settings\\translations.json") as f:
            self.translations = json.load(f)

        self.commands = self.translations["command"]
        self.data = self.translations["data"]
    
    def parse_raw_text(self, raw_str: str) -> dict:
        """Parses text to return useable data
        
        :param raw_str: The raw text to parse
        :return: A dictionary of the function to invoke and data to use, eg:
            {
                "command": "calculator",
                "data": "1 + 2"
            }
        """
        text = raw_str.lower()

        predicted_commands = defaultdict(int)
        for command in self.commands:
            for c in self.commands[command]:
                if c in text:
                    predicted_commands[command] += 1

        predicted_command = ("", float("-inf"))
        for c in predicted_commands:
            if predicted_commands[c] > predicted_command[1]:
                predicted_command = (c, predicted_commands[c])

        for d in self.data:
            text = text.replace(d, self.data[d])

        return {"command": predicted_command[0], "data": text}
    
    def get_input(self, kb_handler: Keyboard_Handler) -> dict:
        """Gets and interprets text input
        
        :param commands: The available commands in the system
        :return: Dictionary of prediction, eg:
            {
                "command": "calculator",
                "data": "1 + 2"
            }
        """
        text = kb_handler.access_text()
        parsed = self.parse_raw_text(text)

        return parsed


class Speech_Input_Handler:
    """Class for handling speech input"""
    def __init__(self):
        logInfo("Speech Input", "Speech Input started")
        self.recognizer = sr.Recognizer()
        with open("settings\\translations.json") as f:
            self.translations = json.load(f)
        
        self.commands = self.translations["command"]
        self.data = self.translations["data"]

    def listen(self, timeout: int = 2) -> sr.AudioData:
        """Listen for audio
        
        :param timeout: Seconds of 'dead time' to wait for audio
        :return: Raw audio data recorded
        """
        with sr.Microphone(device_index=3) as source:
            try:
                return self.recognizer.listen(source, timeout=timeout)
            except sr.WaitTimeoutError as e:
                logError("Speech Input", "No Audio Captured", f"Recognizer failed to capture any audio and timed out: {e}")
                return None

    def parse_raw_audio(self, raw_audio: sr.AudioData) -> dict:
        """Parses raw audio and return useful data
        
        :param raw_audio: The raw audio to parse
        :return: A dictionary of the function to invoke and data to use, eg:
            {
                "command": "calculator",
                "data": "1 + 2"
            }
        """
        try:
            text = self.recognizer.recognize_google(raw_audio)
        except sr.UnknownValueError or sr.RequestError as e:
            logException("Speech Input", e)
            return None
        
        text = text.lower()

        predicted_commands = defaultdict(int)
        for command in self.commands:
            for c in self.commands[command]:
                if c in text:
                    predicted_commands[command] += 1

        predicted_command = ("", float("-inf"))
        for c in predicted_commands:
            if predicted_commands[c] > predicted_command[1]:
                predicted_command = (c, predicted_commands[c])

        for d in self.data:
            text = text.replace(d, self.data[d])

        return {"command": predicted_command[0], "data": text.replace(" ", "")}
