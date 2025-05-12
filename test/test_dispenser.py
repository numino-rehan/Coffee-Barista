import pytest
from model import (Inventory,Menu,Dispenser,CommandProcessor)

from config.constants import DRINK_MENU,MAX_STOCK
from exceptions import (InvalidCommandException, OutOfStockException)


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
    assert f"Dispensing: {drink_name}" in out

def test_dispense_out_of_stock():
    inventory = Inventory()
    inventory.stock = {"Coffee": 1, "Sugar": 0, "Cream": 0}
    dispenser = Dispenser(inventory=inventory)
    drink_name = "Coffee"

    with pytest.raises(OutOfStockException) as exc_info:
        dispenser.dispense(drink_name=drink_name)
    
    assert str(exc_info.value) == f"Out of stock: {drink_name}"
 