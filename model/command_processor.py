import sys
from colorama import Fore

from exceptions.command_processor_exception import InvalidCommandError
from exceptions.dispenser_exception import OutOfStockError
from model.commands.command_context import CommandContext
from model.commands.dispense_command import DispenseCommand
from model.commands.quit_command import QuitCommand
from model.commands.restock_command import RestockCommand
from model.commands.registry_command import CommandRegistry


class CommandProcessor:
    def __init__(self, inventory, menu, dispenser):
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser

        self.context = CommandContext(inventory, menu, dispenser)

        # Setup command registry
        self.registry = CommandRegistry()
        self.registry.register("q", QuitCommand())
        self.registry.register("r", RestockCommand())
        self.registry.register(tuple(self.menu.id_to_drink.keys()), DispenseCommand())
        for i in range(1, 7):
            self.registry.register(str(i), DispenseCommand())

    def process(self, command: str):
        print(self.menu.id_to_drink.keys())
        command = command.strip().lower()
        if not command:
            return
        try:

            commandObj = self.registry.get(command)

            if not commandObj:
                raise InvalidCommandError(command)
            if command.isdigit():
                args = self.menu.id_to_drink[(command)]
            else:
                args = command
            commandObj.execute(args, self.context)
        except Exception as e:
            print(Fore.RED + str(e))
            print()
