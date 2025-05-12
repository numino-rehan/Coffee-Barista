from config.constants import DRINK_MENU, INGREDIENT_PRICES
from exceptions import (IngredientMismatchError)

from colorama import Fore, Style

class Menu:
    def __init__(self, inventory):
        self.drink_menu = DRINK_MENU
        self.inventory = inventory
        self.id_to_drink = self._map_ids_to_drinks()
        self.menu = self._build_menu()

    def _map_ids_to_drinks(self):
        return {str(i): drink for i, drink in enumerate(sorted(self.drink_menu), 1)}

    def _build_menu(self):
        menu = {}
        for i, drink in enumerate(sorted(self.drink_menu), 1):
            try:
                cost = self._calculate_cost(self.drink_menu[drink])
                available = self.inventory.has_ingredients(self.drink_menu[drink])
            except IngredientMismatchError as e:
                cost = 0
                available = False
            menu[drink] = {
                "item_id": i,
                "cost": round(cost, 2),
                "in_stock": available,
            }
        return menu

    def _calculate_cost(self, recipe: dict) -> float:
        try:
            return sum(INGREDIENT_PRICES[ing] * qty for ing, qty in recipe.items())
        except KeyError as e:
            raise IngredientMismatchError(str(e))

    def get_menu(self):
        """Return the current menu data."""
        return self.menu

    def refresh(self):
        """Recalculate availability and pricing based on current inventory."""
        self.menu = self._build_menu()

    def get_drink_by_id(self, item_id: str):
        return self.id_to_drink.get(item_id)
    
    def display_menu(self):
        print(Fore.BLUE + Style.BRIGHT + "\nMENU:")
        for drink, val in self.get_menu().items():
            price = f"${val['cost']:.2f}"
            available = Fore.GREEN + "Yes" if val["in_stock"] else Fore.RED + "No"
            item_id = val["item_id"]
            print(
                f"{Fore.YELLOW}{item_id}{Style.RESET_ALL}, {drink}, "
                f"{Fore.CYAN}{price}{Style.RESET_ALL}, Available: {available}"
            )
        print()
