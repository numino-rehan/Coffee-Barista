"""
main.py

Entry point for the Coffee Machine CLI application.
Initializes the inventory, menu, dispenser, and command processor,
and runs an interactive command loop to process user commands.
"""
from exceptions import (
    OutOfStockException,
    DrinkNotFoundException,
    IngredientMismatchException,
    InvalidCommandException
)
from models import Menu, Dispenser, Inventory
from services.command_processor import CommandProcessor
from utils import setup_logger

logger = setup_logger("main")


def run_coffee_machine():
    """
    Starts the interactive coffee machine command loop.

    Initializes necessary components and continuously prompts
    the user to enter commands to order drinks, restock inventory,
    or quit the application.

    Logs errors encountered during command processing.
    """
    inventory = Inventory()
    menu = Menu(inventory)
    dispenser = Dispenser(inventory)
    processor = CommandProcessor(inventory, menu, dispenser)

    logger.info("Welcome to the Coffee Machine!")

    while True:
        try:
            print("\nCurrent Inventory:\n")
            inventory.display_inventory()
            print("\nAvailable Drinks:\n")
            menu.display_menu()
            command = input(
                "Enter command (ID to order, 'r' to restock, 'q' to quit): ")
            processor.process(command)
        except OutOfStockException as e:
            print(f"{e}\n")
        except InvalidCommandException as e:
            print(f"{e}\n")
        except DrinkNotFoundException as e:
            print(f"{e}\n")
        except IngredientMismatchException as e:
            print(f"{e}\n")
        except Exception as error:
            print(f"{error}\n")


if __name__ == "__main__":
    run_coffee_machine()
