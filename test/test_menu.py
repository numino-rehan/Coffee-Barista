from config.constants import DRINK_MENU, INGREDIENT_PRICES
from models import Inventory, Menu


def test_menu_structure_and_prices():
    """Test if the menu structure is correct and the prices are calculated correctly."""
    inventory = Inventory()
    menu = Menu(inventory)
    menu_data = menu.get_menu()

    for drink, config in DRINK_MENU.items():
        assert drink in menu_data
        expected_cost = round(
            sum(
                INGREDIENT_PRICES[ingredient] * qty
                for ingredient, qty in config.items()
            ),
            2,
        )
        assert menu_data[drink]["cost"] == expected_cost


def test_drink_availability_initially_true():
    """Test if drinks are available initially if the inventory has full stock."""
    inventory = Inventory()
    menu = Menu(inventory)
    menu_data = menu.get_menu()

    # Initially, all drinks should be in stock
    for drink in menu_data:
        assert menu_data[drink]["in_stock"] is True


def test_each_drink_cost_matches_config():
    inventory = Inventory()
    menu = Menu(inventory)
    menu_data = menu.get_menu()

    for drink, ingredients in DRINK_MENU.items():
        expected_cost = round(
            sum(
                INGREDIENT_PRICES[ingredient] * qty
                for ingredient, qty in ingredients.items()
            ),
            2,
        )
        assert menu_data[drink]["cost"] == expected_cost, f"{drink} cost mismatch"


def test_all_drinks_available_with_full_stock():
    inventory = Inventory()
    menu = Menu(inventory)
    menu_data = menu.get_menu()

    for drink in DRINK_MENU:
        assert menu_data[drink]["in_stock"] is True, f"{drink} should be in stock"


def test_drink_unavailable_when_ingredient_missing():
    inventory = Inventory()
    inventory.stock["Whipped Cream"] = 0  # Used in "Caffe Mocha"

    menu = Menu(inventory)
    menu_data = menu.get_menu()

    assert (
        menu_data["Caffe Mocha"]["in_stock"] is False
    ), "Caffe Mocha should be unavailable"


def test_partial_availability_of_drinks():
    inventory = Inventory()
    inventory.stock["Cocoa"] = 0  # Only affects "Caffe Mocha"

    menu = Menu(inventory)
    menu_data = menu.get_menu()

    assert menu_data["Caffe Mocha"]["in_stock"] is False
    assert menu_data["Caffe Latte"]["in_stock"] is True
