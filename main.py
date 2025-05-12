from model.inventory import Inventory
from model.menu import Menu
from model.dispenser import Dispenser
from model.command_processor import CommandProcessor
from colorama import Fore, Style, init

init(autoreset=True)


def run_coffee_machine():
    inventory = Inventory()
    menu = Menu(inventory)
    dispenser = Dispenser(inventory)
    processor = CommandProcessor(inventory, menu, dispenser)
    print(Fore.RED + "Hello")
    while True:
        try:
            inventory.display_inventory()
            menu.display_menu()
            command = input(Fore.YELLOW + "Enter command (ID to order, 'r' to restock, 'q' to quit): ")
            processor.process(command)
        except Exception as e:
            print(Fore.RED + f"{e}")

if __name__ == "__main__":
    run_coffee_machine()
