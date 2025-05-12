class DispenserException(Exception):
    """Base class for dispenser-related errors."""
    pass


class OutOfStockException(DispenserException):
    def __init__(self, drink_name=None):
        msg = f"Out of stock" + (f": {drink_name}" if drink_name else "")
        super().__init__(msg)
