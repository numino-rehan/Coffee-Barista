import sys
from colorama import Fore
from utils.exceptions import (
    InvalidCommandError,
    OutOfStockError,
)
from utils.helper import log_and_print

class CommandProcessor:
    def __init__(self, inventory, menu, dispenser):
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser

    def process(self, command: str):
        command = command.strip().lower()
        if not command:
            return

        if command == "q":
            print(Fore.YELLOW + "Exiting the Coffee Machine. Goodbye!")
            sys.exit()
        elif command == "r":
            print(Fore.CYAN + "Restocking ingredients...")
            self.inventory.restock()
            self.menu.refresh()
        elif command in self.menu.id_to_drink:
            drink = self.menu.get_drink_by_id(command)
            try:
                self.dispenser.dispense(drink)
                self.menu.refresh()
            except OutOfStockError as e:
                print(Fore.RED + str(e))
        else:
            raise InvalidCommandError(command)
