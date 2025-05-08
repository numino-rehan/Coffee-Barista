class CoffeeMachineError(Exception):
    """Base class for all coffee machine exceptions."""
    pass


class OutOfStockError(CoffeeMachineError):
    """Raised when ingredients are insufficient to make a drink."""
    def __init__(self, drink_name=None):
        msg = f"Out of stock" + (f": {drink_name}" if drink_name else "")
        super().__init__(msg)


class InvalidCommandError(CoffeeMachineError):
    """Raised when the user inputs an invalid command."""
    def __init__(self, command):
        super().__init__(f"Invalid command: '{command}'")


class IngredientMismatchError(CoffeeMachineError):
    """Raised if the ingredient in recipe is not defined in stock."""
    def __init__(self, ingredient):
        super().__init__(f"Unknown ingredient in recipe: {ingredient}")
