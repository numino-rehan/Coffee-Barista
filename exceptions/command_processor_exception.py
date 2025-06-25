
from utils import setup_logger

logger = setup_logger("command_processor_exception")

class CommandException(Exception):
    """Base class for command-related errors."""
    pass


class InvalidCommandException(CommandException):
    """Exception raised when an invalid command is encountered."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

