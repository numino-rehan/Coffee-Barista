"""
main.py

Entry point for the Coffee Machine CLI application.
Initializes the inventory, menu, dispenser, and command processor,
and runs an interactive command loop to process user commands.
"""

from colorama import Fore, Style

from exceptions import (DrinkNotFoundException, IngredientMismatchException,
                        InvalidCommandException, OutOfStockException)
from services.command_processor import CommandProcessor
from utils import setup_logger

logger = setup_logger("main")


def print_error(message: str):
    """
    Helper to print error messages in red color.
    """
    print(Fore.RED + message + Style.RESET_ALL + "\n")


def run_coffee_machine():
    """
    Starts the interactive coffee machine command loop.

    Initializes necessary components and continuously prompts
    the user to enter commands to order drinks, restock inventory,
    or quit the application.

    Logs errors encountered during command processing.
    """

    processor = CommandProcessor()

    logger.info("Welcome to the Coffee Machine!")

    while True:
        try:
            print("\nCurrent Inventory:\n")
            processor.inventory.display_inventory()

            print("\nAvailable Drinks:\n")
            processor.menu.display_menu()

            command = input(
                "Enter command (ID to order, 'r' to restock, 'q' to quit): ").strip()

            processor.process(command)

        except OutOfStockException as e:
            logger.warning(f"Out of stock: {e}")
            print_error(
                "Selected drink is out of stock. Please choose another.")

        except InvalidCommandException as e:
            logger.warning(f"Invalid command: {e}")
            print_error(
                "Invalid command. Please try again with a valid input.")

        except DrinkNotFoundException as e:
            logger.warning(f"Drink not found: {e}")
            print_error("The selected drink ID does not exist.")

        except IngredientMismatchException as e:
            logger.warning(f"Ingredient mismatch: {e}")
            print_error(
                "Unable to prepare the drink due to mismatched ingredients.")

        except SystemExit:
            print(Fore.GREEN + "Exiting Coffee Machine. Goodbye!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    run_coffee_machine()
