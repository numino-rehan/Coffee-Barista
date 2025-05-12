
INGREDIENT_PRICES = {
    "Coffee": 0.75,
    "Decaf Coffee": 0.75,
    "Sugar": 0.25,
    "Cream": 0.25,
    "Steamed Milk": 0.35,
    "Foamed Milk": 0.35,
    "Espresso": 1.10,
    "Cocoa": 0.90,
    "Whipped Cream": 1.00,
}

DRINK_MENU = {
    "Coffee": {"Coffee": 3, "Sugar": 1, "Cream": 1},
    "Decaf Coffee": {"Decaf Coffee": 3, "Sugar": 1, "Cream": 1},
    "Caffe Latte": {"Espresso": 2, "Steamed Milk": 1},
    "Caffe Americano": {"Espresso": 3},
    "Caffe Mocha": {"Espresso": 1, "Cocoa": 1, "Steamed Milk": 1, "Whipped Cream": 1},
    "Cappuccino": {"Espresso": 2, "Steamed Milk": 1, "Foamed Milk": 1},
}

MAX_STOCK = 10


COMMAND_LIST = {
    "quit": "q",
    "restock": "r",
}
