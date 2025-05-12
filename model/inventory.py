from config.constants import INGREDIENT_PRICES, MAX_STOCK,COMMAND_LIST
from exceptions import (InvalidCommandException, OutOfStockException,IngredientMismatchException)

from colorama import Fore, Style

class Inventory:
    def __init__(self):
        # Initialize stock to MAX_STOCK for each ingredient
        self.stock = {ingredient: MAX_STOCK for ingredient in sorted(INGREDIENT_PRICES)}

    def restock(self):
        """Restock all ingredients to MAX_STOCK."""
        self.stock = {ingredient: MAX_STOCK for ingredient in self.stock}

    def has_ingredients(self, recipe: dict) -> bool:
        """Check if enough ingredients are available for a recipe."""
        for ing, qty in recipe.items():
            if ing not in self.stock:
                raise IngredientMismatchException(ing)
            if self.stock[ing] < qty:
                return False
        return True

    def deduct_ingredients(self, recipe: dict):
        """Deduct the required ingredients for a recipe from inventory."""
        if not self.has_ingredients(recipe):
            raise OutOfStockException()
        for ing, qty in recipe.items():
            self.stock[ing] -= qty

    def get_stock(self) -> dict:
        """Return a copy of current stock levels."""
        return self.stock.copy()
    
    def display_inventory(self):
        print(self)
        print()

    def __str__(self):
        lines = [Fore.MAGENTA + Style.BRIGHT + "\nINVENTORY:" + Style.RESET_ALL]
        for item, qty in self.get_stock().items():
            lines.append(f"{item} {qty}")
        return "\n".join(lines)
