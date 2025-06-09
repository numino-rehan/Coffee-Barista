from colorama import Fore, Style
from utils.loger_config import setup_logger

logger = setup_logger("inventory-exception")


class InventoryException(Exception):
    """Base class for inventory-related errors."""
    pass


class IngredientMismatchException(InventoryException):
    """Exception raised when there is a mismatch in ingredient availability."""

    def __init__(self, ingredient):
        msg = Fore.RED + f"{ingredient}" + Style.RESET_ALL
        super().__init__(msg)
