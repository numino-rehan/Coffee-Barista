from colorama import Fore, Style

from config.constants import DRINK_MENU
from exceptions import DrinkNotFoundException, OutOfStockException
from utils import log_execution, setup_logger

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

    @log_execution
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
            logger.error(f"No recipe found for drink '{drink_name}'")
            raise DrinkNotFoundException(drink_name)

        if not self.inventory.has_ingredients(recipe):
            logger.error(f"Out of stock for drink '{drink_name}'")
            raise OutOfStockException(drink_name)

        self.inventory.deduct_ingredients(recipe)
        logger.info(f"Dispensing drink: {drink_name}")
        logger.info(
            Fore.GREEN + f"Successfully dispensed drink: {drink_name}" + Style.RESET_ALL)
        print(Fore.GREEN +
              f"Enjoy your {drink_name}!" + Style.RESET_ALL + "\n")
