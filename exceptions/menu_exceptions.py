
from utils import setup_logger

logger = setup_logger("inventory-exception")


class MenuException(Exception):
    """Base class for menu-related errors."""
    pass



class DrinkNotFoundException(MenuException):
    """Exception raised when a drink is not found in the menu."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)