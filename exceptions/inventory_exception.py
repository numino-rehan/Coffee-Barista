
from utils import setup_logger

logger = setup_logger("inventory-exception")


class InventoryException(Exception):
    """Base class for inventory-related errors."""
    pass


class IngredientMismatchException(InventoryException):
    """Exception raised when there is a mismatch in ingredient availability."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
