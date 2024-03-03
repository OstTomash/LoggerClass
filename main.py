class Logger:
    """A simple class that logs messages with specific log_level.

    This class allow users print messages to console with predefined log_level.

    Attributes:
        - log_level(str): The log level

    Methods:
        - __init__(log_level): Initializes the logger with the specified log_level
        - __call__(message): Prints the message to the console with the predefined log_level

    Example usage:
        >>> logger = Logger("Info")
        >>> logger("Something happened!")
        Info: Something happened!
    """
    def __init__(self, log_level):
        """Initializes the logger with the log_level attribute"""
        self.log_level = log_level

    def __call__(self, message):
        """Prints the message to the console with the predefined log_level"""
        print(f'{self.log_level}: {message}')


logger = Logger("Info")
logger("Something happened!")
