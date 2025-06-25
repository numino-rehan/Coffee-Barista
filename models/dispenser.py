from colorama import Fore, Style

from config.constants import DRINK_MENU
from exceptions import DrinkNotFoundException, OutOfStockException
from utils import log_and_handle_errors, setup_logger

from .inventory import Inventory

logger = setup_logger("dispenser")


class Dispenser:
    """
    Handles dispensing drinks by checking inventory and deducting ingredients.
    """

    def __init__(self, inventory: Inventory):
        """
        Initialize the dispenser with the given inventory instance.

        Args:
            inventory: Inventory instance managing ingredient stock.
        """
        self.inventory = inventory

    @log_and_handle_errors("Failed to dispense drink")
    def dispense(self, drink_name: str):
        """
        Dispense a drink if the ingredients are available.

        Args:
            drink_name (str): Name of the drink to dispense.

        Raises:
            DrinkNotFoundException: If the recipe for the drink does not exist.
            OutOfStockException: If there are not enough ingredients.
        """
        recipe = DRINK_MENU.get(drink_name)
        if not recipe:
            message = f"No recipe found for drink '{drink_name}'"
            logger.error(message)
            raise DrinkNotFoundException(message)

        if not self.inventory.has_ingredients(recipe):
            message = f"Not enough ingredients to make '{drink_name}'"
            logger.error(message)
            raise OutOfStockException(message)

        self.inventory.deduct_ingredients(recipe)
        logger.info(f"Dispensing drink: {drink_name}")
        print(Fore.GREEN + f"Enjoy your {drink_name}!" + Style.RESET_ALL + "\n")
