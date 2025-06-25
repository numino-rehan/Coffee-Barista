
from utils import setup_logger

logger = setup_logger("dispenser-exception")


class DispenserException(Exception):
    """Base class for dispenser-related errors."""
    pass


class OutOfStockException(DispenserException):
    """Exception raised when a requested drink is out of stock."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
