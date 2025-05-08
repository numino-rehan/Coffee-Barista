from config.constants import DRINK_MENU
from utils.helper import log_and_print
from utils.exceptions import OutOfStockError


class Dispenser:
    def __init__(self, inventory):
        self.inventory = inventory

    def dispense(self, drink_name: str):
        """Dispense a drink if ingredients are available."""
        recipe = DRINK_MENU.get(drink_name)
        if not recipe:
            raise ValueError(f"No recipe found for '{drink_name}'")

        if not self.inventory.has_ingredients(recipe):
            raise OutOfStockError(drink_name)

        self.inventory.deduct_ingredients(recipe)
        log_and_print(f"Dispensing: {drink_name}")


