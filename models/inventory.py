from typing import Dict

from colorama import Fore, Style

from config.constants import INGREDIENT_PRICES, MAX_STOCK
from exceptions import IngredientMismatchException, OutOfStockException
from utils import log_and_handle_errors, setup_logger

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

    @log_and_handle_errors("Failed to restock inventory")
    def restock(self) -> None:
        """
        Restock all ingredients to MAX_STOCK.
        """
        self.stock = {ingredient: MAX_STOCK for ingredient in self.stock}
        logger.info(Fore.GREEN + "Inventory restocked to max levels." + Style.RESET_ALL)
        print(Fore.GREEN + "Inventory restocked to max levels." + Style.RESET_ALL)

    @log_and_handle_errors("Failed to check ingredient availability")
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
                message = f"Ingredient '{ingredient}' not found in inventory."
                logger.error(message)
                raise IngredientMismatchException(message)
            if self.stock[ingredient] < quantity:
                logger.warning(
                    f"Insufficient stock for '{ingredient}': "
                    f"required={quantity}, available={self.stock[ingredient]}"
                )
                return False
        return True

    @log_and_handle_errors("Failed to deduct ingredients")
    def deduct_ingredients(self, recipe: Dict[str, int]) -> None:
        """
        Deduct the required ingredients for a recipe from inventory.

        Args:
            recipe (Dict[str, int]): Ingredients and quantities to deduct.

        Raises:
            OutOfStockException: If any ingredient is insufficient.
        """
        if not self.has_ingredients(recipe):
            message = "Insufficient ingredients to complete the operation."
            logger.error(message)
            raise OutOfStockException(message)

        for ingredient, quantity in recipe.items():
            self.stock[ingredient] -= quantity
        logger.info(f"Deducted ingredients: {recipe}")

    @log_and_handle_errors("Failed to retrieve inventory stock")
    def get_stock(self) -> Dict[str, int]:
        """
        Return a copy of the current stock levels.

        Returns:
            Dict[str, int]: Current stock of ingredients.
        """
        return self.stock.copy()

    @log_and_handle_errors("Failed to display inventory")
    def display_inventory(self) -> None:
        """
        Log the current inventory stock.
        """
        logger.info(str(self))

    @log_and_handle_errors("Failed to generate inventory string representation")
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
