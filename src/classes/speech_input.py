"""Base class for speech recognition and translation"""

# My functions
from ..helpers import *

# Builtin
from typing import List
from os import PathLike

# Not builtin
try:
    import speech_recognition as sr
    import pyaudio
except ImportError as e:
    logException("Speech Input", e)
    print("Uninstalled package, try `pip install SpeechRecognition` or `pip install pyaudio`")
    quit()


class Speech_Input_Handler:
    """Class for handling speech input"""
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def parse_audio(self, audio: sr.AudioData) -> str:
        """Parse microphone audio, only using sphinx at the moment

        :param audio: The AudioData from the microphone
        :return: The raw data from the recognizer
        """
        try:
            return self.recognizer.recognize_sphinx(audio)
        except sr.UnknownValueError or sr.RequestError as e:
            logException("Speech Input", e)
            return None

    def parse_raw(self, raw_str: str, translations: PathLike) -> dict:
        text = raw_str.lower()
    
    def get_input(self, commands: List[str], translations: PathLike = "translations.json") -> dict:
        """Gets and interprets microphone input
        
        :param commands: The available commands in the system
        :param translations: Path to the json file of translations
        :return: Dictionary of prediction, eg:
                {
                    "command": "calculator",
                    "data": "1 + 2"
                }
        """
        # Listen to user
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        # Recognize
        raw_data = self.parse_audio(audio)
        if raw_data is None:
            return None
        
        # Parse
        parsed = self.parse_raw(raw_data, translations)
