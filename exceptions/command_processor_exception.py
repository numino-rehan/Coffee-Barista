class CommandException(Exception):
    """Base class for command-related errors."""
    pass


class InvalidCommandException(CommandException):
    def __init__(self, command):
        super().__init__(f"Invalid command: '{command}'")
