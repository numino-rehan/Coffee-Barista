class InventoryException(Exception):
    """Base class for inventory-related errors."""
    pass


class IngredientMismatchException(InventoryException):
    def __init__(self, ingredient):
        super().__init__(f"Unknown ingredient in inventory: {ingredient}")
