from typing import Dict, Optional

from config.constants import DRINK_MENU, INGREDIENT_PRICES
from exceptions import IngredientMismatchException
from .inventory import Inventory
from utils import setup_logger,log_execution

logger = setup_logger("menu")


class Menu:
    """
    Handles the drink menu, including pricing and availability based on inventory.
    """

    def __init__(self, inventory: Inventory):
        """
        Initialize the Menu with a reference to inventory.

        Args:
            inventory: Inventory instance to check ingredient availability.
        """
        self.drink_menu = DRINK_MENU
        self.inventory = inventory
        self.sorted_drinks = sorted(self.drink_menu)
        self.id_to_drink = {str(i): drink for i,
                            drink in enumerate(self.sorted_drinks, 1)}
        self.menu = self._build_menu()
        logger.info("Menu initialized.")

    def _map_ids_to_drinks(self) -> Dict[str, str]:
        """
        Map string IDs to drink names.

        Returns:
            dict: Mapping of string item IDs to drink names.
        """
        # This method now unused but kept for backward compatibility if needed
        return {str(i): drink for i, drink in enumerate(self.sorted_drinks, 1)}

    @log_execution
    def _build_menu(self) -> Dict[str, Dict]:
        """
        Build the current menu with cost and availability information.

        Returns:
            dict: Menu data with drink details.
        """
        menu = {}
        for i, drink in enumerate(self.sorted_drinks, 1):
            try:
                cost = self._calculate_cost(self.drink_menu.get(drink, {}))
                available = self.inventory.has_ingredients(
                    self.drink_menu.get(drink, {}))
            except IngredientMismatchException as e:
                logger.error(f"Ingredient mismatch for drink '{drink}': {e}")
                cost = 0
                available = False
            menu[drink] = {
                "item_id": i,
                "cost": round(cost, 2),
                "in_stock": available,
            }
        logger.debug(f"Menu built: {menu}")
        return menu

    def _calculate_cost(self, recipe: dict) -> float:
        """
        Calculate the cost of a drink recipe based on ingredient prices.

        Args:
            recipe (dict): Ingredients and quantities.

        Returns:
            float: Total cost of the drink.

        Raises:
            IngredientMismatchException: If an ingredient price is missing.
        """
        cost = 0.0
        for ing, qty in recipe.items():
            price = INGREDIENT_PRICES.get(ing)
            if price is None:
                logger.error(f"Ingredient price missing for: {ing}")
                raise IngredientMismatchException(str(ing))
            cost += price * qty
        return cost

    def get_menu(self) -> Dict[str, Dict]:
        """
        Get the current menu data.

        Returns:
            dict: Current menu with drinks info.
        """
        return self.menu

    def refresh(self) -> Dict[str, Dict]:
        """
        Recalculate availability and pricing based on current inventory.

        Returns:
            dict: Updated menu with drinks info.
        """
        self.menu = self._build_menu()
        logger.info("Menu refreshed.")
        return self.menu

    def get_drink_by_id(self, item_id: str) -> Optional[str]:
        """
        Get the drink name for a given item ID.

        Args:
            item_id (str): The string ID of the drink.

        Returns:
            str or None: Drink name or None if not found.
        """
        drink = self.id_to_drink.get(item_id)
        if drink is None:
            logger.warning(f"Requested invalid drink ID: {item_id}")
        return drink

    def display_menu(self) -> None:
        """
        Log the current menu.
        """
        logger.info(self.__str__())

    def __str__(self) -> str:
        """
        String representation of the menu.

        Returns:
            str: Formatted string showing menu details.
        """
        menu = self.get_menu()
        if not menu:
            return "Menu is currently unavailable."

        lines = ["MENU:"]
        for drink, val in menu.items():
            price = val.get("cost", 0.0)
            available = val.get("in_stock", False)
            item_id = val.get("item_id", "?")
            price_str = f"${price:.2f}" if isinstance(
                price, (int, float)) else "$0.00"
            availability_str = "Yes" if available else "No"
            lines.append(
                f"{item_id}: {drink}, Price: {price_str}, Available: {availability_str}")

        return "\n".join(lines)
