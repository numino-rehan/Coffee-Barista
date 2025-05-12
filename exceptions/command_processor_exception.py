class CommandError(Exception):
    """Base class for command-related errors."""
    pass


class InvalidCommandError(CommandError):
    def __init__(self, command):
        super().__init__(f"Invalid command: '{command}'")
