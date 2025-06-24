import pytest

from config.constants import DRINK_MENU, MAX_STOCK
from exceptions import OutOfStockException
from models import Dispenser, Inventory


def test_dispense_success(capfd):
    inventory = Inventory()
    dispenser = Dispenser(inventory)

    drink_name = "Coffee"
    dispenser.dispense(drink_name)

    # Check inventory deducted
    for ingredient, qty in DRINK_MENU[drink_name].items():
        assert inventory.stock[ingredient] == MAX_STOCK - qty

    # Check log message
    out, _ = capfd.readouterr()
    print("-->", out)
    assert f"Enjoy your {drink_name}" in out


def test_dispense_out_of_stock():
    inventory = Inventory()
    inventory.stock = {"Coffee": 1, "Sugar": 0, "Cream": 0}
    dispenser = Dispenser(inventory=inventory)
    drink_name = "Coffee"

    with pytest.raises(OutOfStockException) as exc_info:
        dispenser.dispense(drink_name=drink_name)
    print("--> ss", str(exc_info.value))

    assert f"Out of stock: {drink_name}" in str(exc_info.value)
