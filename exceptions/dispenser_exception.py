from colorama import Fore, Style

from utils import setup_logger

logger = setup_logger("dispenser-exception")


class DispenserException(Exception):
    """Base class for dispenser-related errors."""
    pass


class OutOfStockException(DispenserException):
    """Exception raised when a requested drink is out of stock."""
    def __init__(self, drink_name=None):
        msg = Fore.RED + "Out of stock" + (f": {drink_name}" if drink_name else "") + Style.RESET_ALL
        super().__init__(msg)
