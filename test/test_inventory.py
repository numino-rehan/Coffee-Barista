from model.inventory import Inventory
import pytest
from config.constants import MAX_STOCK

from exceptions.dispenser_exception import OutOfStockError
from exceptions.inventory_exception import IngredientMismatchError

def test_initial_stock():
    inventory = Inventory()
    stock = inventory.get_stock()
    assert all(qty == MAX_STOCK for qty in stock.values())


def test_has_ingredients_true():
    inventory = Inventory()
    inventory.stock = {"coffee": 2, "milk": 1}
    recipe = {"coffee": 2, "milk": 1}
    assert inventory.has_ingredients(recipe) is True


def test_has_ingredients_mismatch_error():
    inventory = Inventory()
    inventory.stock = {"coffee": 1, "milk": 1}
    recipe = {"foam": 2, "milk": 1}
    with pytest.raises(IngredientMismatchError) as exc_info:
        inventory.has_ingredients(recipe)
    print(f"INfo {exc_info.value}")
    assert "foam" in str(exc_info.value)

def test_has_ingredients_false():
    inventory = Inventory()
    inventory.stock = {"coffee": 1, "milk": 1}
    recipe = {"coffee": 2, "milk": 1}
    assert inventory.has_ingredients(recipe) is False

def test_deduct_ingredients_success():
    inventory = Inventory()
    inventory.stock = {"coffee": 3, "milk": 1}
    recipe = {"coffee": 2, "milk": 1}
    inventory.deduct_ingredients(recipe)
    assert inventory.stock["coffee"] == 1
    assert inventory.stock["milk"] == 0


def test_deduct_ingredients_out_of_stock_error():
    inventory = Inventory()
    inventory.stock = {"coffee": 1}
    recipe = {"coffee": 3}
    with pytest.raises(OutOfStockError):
        inventory.deduct_ingredients(recipe)

def test_restock_resets_to_max():
    inventory = Inventory()
    inventory.stock["coffee"] = 0
    inventory.restock()
    assert all(qty == MAX_STOCK for qty in inventory.get_stock().values())

def test_get_stock_returns_copy():
    inventory = Inventory()
    inventory.stock = {"coffee": 1}
    stock_copy = inventory.get_stock()
    stock_copy["coffee"] = 0
    assert inventory.stock["coffee"] == 1


