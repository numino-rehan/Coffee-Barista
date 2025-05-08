from core.inventory import Inventory
from core.menu import Menu
from core.dispenser import Dispenser
from core.command_processor import CommandProcessor
from utils.exceptions import CoffeeMachineError
from colorama import Fore, Style, init

init(autoreset=True)

def display_inventory(inventory):
    print(Fore.MAGENTA + Style.BRIGHT + "\nINVENTORY:")
    for item, qty in inventory.get_stock().items():
        print(f"{item} {qty}")
    print("")

def display_menu(menu):
    print(Fore.BLUE + Style.BRIGHT + "\nMENU:")
    for drink, val in menu.get_menu().items():
        price = f"${val['cost']:.2f}"
        available = Fore.GREEN + "Yes" if val["in_stock"] else Fore.RED + "No"
        item_id = val["item_id"]
        print(
            f"{Fore.YELLOW}{item_id}{Style.RESET_ALL}, {drink}, "
            f"{Fore.CYAN}{price}{Style.RESET_ALL}, Available: {available}"
        )
    print()

def run_coffee_machine():
    inventory = Inventory()
    menu = Menu(inventory)
    dispenser = Dispenser(inventory)
    processor = CommandProcessor(inventory, menu, dispenser)

    while True:
        try:
            display_inventory(inventory)
            display_menu(menu)
            command = input(Fore.YELLOW + "Enter command (ID to order, 'r' to restock, 'q' to quit): ")
            processor.process(command)
        except CoffeeMachineError as e:
            print(Fore.RED + f"[Error] {e}")
        except Exception as e:
            print(Fore.RED + f"[Unhandled Error] {e}")

if __name__ == "__main__":
    run_coffee_machine()
