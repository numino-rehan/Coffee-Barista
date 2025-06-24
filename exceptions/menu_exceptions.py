from colorama import Fore, Style

from utils import setup_logger

logger = setup_logger("inventory-exception")


class MenuException(Exception):
    """Base class for menu-related errors."""
    pass



class DrinkNotFoundException(MenuException):
    """Exception raised when a drink is not found in the menu."""

    def __init__(self, drink_name):
        msg = Fore.RED + f"Drink '{drink_name}' not found in menu." + Style.RESET_ALL
        super().__init__(msg)