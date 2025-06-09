from colorama import Fore, Style
from utils import setup_logger

logger = setup_logger("command_processor_exception")

class CommandException(Exception):
    """Base class for command-related errors."""
    pass


class InvalidCommandException(CommandException):
    """Exception raised when an invalid command is encountered."""
    def __init__(self, command):
        msg = Fore.RED + f"Invalid command: '{command}'" + Style.RESET_ALL
        super().__init__(msg)

