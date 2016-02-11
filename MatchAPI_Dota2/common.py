"""Contains common functions used throughout the codebase"""
from time import strftime, gmtime


def log(message):
    """Logs a message to console
    :param message: the message to print out
    """
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print("{0}: {1}".format(time, message))
