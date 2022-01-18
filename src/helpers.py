"""Helper functions, for use in all programs"""

# Builtins
import sys
import time

# For strftime
TIME_FMT = "%d-%m-%Y@%H:%M:%S"


def logInfo(source: str, msg: str):
    """For logging generic information about processes

    :param source: Where the message came from (ie., Calculator)
    :param msg: Message to log (ie., Process started)
    """

    with open("logs\info.log", 'a') as f:
        # Saves [time] [source] [msg]
        f.write(f"[{time.strftime(TIME_FMT)}]\t[{source}]\t[{msg}]\n")


def logError(source: str, title: str, desc: str):
    """For logging errors in the program (ie., bad user input)
    
    :param source: Where the error came from (ie., Calculator)
    :param title: Simple title of the error (ie., Bad input)
    :param desc: More verbose description of the error
    """

    with open("logs\errors.log", 'a') as f:
        # Saves [time] [source] [title] [description]
        f.write(f"[{time.strftime(TIME_FMT)}]\t[{source}]\t[{title}]\t[{desc}]\n")


def logException(source: str, e: Exception):
    """For logging exceptions at runtime

    :param source: Where the error came from (ie., Calculator)
    :param e: The `Exception` object
    """

    with open("logs\exceptions.log", 'a') as f:
        # Saves [time] [source:line number] [error]
        lineno = sys.exc_info()[-1].tb_lineno
        f.write(f"[{time.strftime(TIME_FMT)}]\t[{source}:{lineno}]\t[{str(e)}]\n")
