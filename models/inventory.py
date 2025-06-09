from typing import Dict

from colorama import Fore, Style
from config.constants import INGREDIENT_PRICES, MAX_STOCK
from exceptions import OutOfStockException, IngredientMismatchException
from utils import setup_logger, log_execution

logger = setup_logger("inventory")


class Inventory:
    """
    Manages the stock of ingredients for the coffee machine.
    """

    def __init__(self) -> None:
        """
        Initialize the inventory with max stock levels for each ingredient.
        """
        self.stock: Dict[str, int] = {
            ingredient: MAX_STOCK for ingredient in sorted(INGREDIENT_PRICES)
        }
        logger.info("Inventory initialized with max stock levels.")

    @log_execution
    def restock(self) -> None:
        """
        Restock all ingredients to MAX_STOCK.
        """
        self.stock = {ingredient: MAX_STOCK for ingredient in self.stock}
        logger.info(
            Fore.GREEN + "Inventory restocked to max levels." + Style.RESET_ALL)
        print(Fore.GREEN + "Inventory restocked to max levels." + Style.RESET_ALL)

    def has_ingredients(self, recipe: Dict[str, int]) -> bool:
        """
        Check if enough ingredients are available for the given recipe.

        Args:
            recipe (Dict[str, int]): Ingredients and quantities required.

        Returns:
            bool: True if all ingredients are available in required quantity, else False.

        Raises:
            IngredientMismatchException: If a required ingredient is not found in stock.
        """
        for ingredient, quantity in recipe.items():
            if ingredient not in self.stock:
                logger.error(
                    f"Ingredient mismatch: '{ingredient}' not found in inventory."
                )
                raise IngredientMismatchException(ingredient)
            if self.stock[ingredient] < quantity:
                logger.warning(
                    f"Insufficient stock for ingredient '{ingredient}': required {quantity}, available {self.stock[ingredient]}"
                )
                return False
        return True

    def deduct_ingredients(self, recipe: Dict[str, int]) -> None:
        """
        Deduct the required ingredients for a recipe from inventory.

        Args:
            recipe (Dict[str, int]): Ingredients and quantities to deduct.

        Raises:
            OutOfStockException: If any ingredient is insufficient.
        """
        if not self.has_ingredients(recipe):
            logger.error("Cannot deduct ingredients: insufficient stock.")
            raise OutOfStockException()
        for ingredient, quantity in recipe.items():
            self.stock[ingredient] -= quantity
        logger.info(f"Deducted ingredients: {recipe}")

    def get_stock(self) -> Dict[str, int]:
        """
        Return a copy of the current stock levels.

        Returns:
            Dict[str, int]: Current stock of ingredients.
        """
        return self.stock.copy()

    def display_inventory(self) -> None:
        """
        Log the current inventory stock and optionally print for user.
        """
        logger.info(self.__str__())
        # Uncomment below line to also print inventory to user console
        # print(self.__str__())

    def __str__(self) -> str:
        """
        String representation of the current inventory.

        Returns:
            str: Formatted inventory stock string.
        """
        lines = ["INVENTORY:"]
        for ingredient, quantity in self.get_stock().items():
            lines.append(f"{ingredient}: {quantity}")
        return "\n".join(lines)
