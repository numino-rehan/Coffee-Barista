import sys
from colorama import Fore

from exceptions import (InvalidCommandException)

from command_core import (CommandContext,CommandRegistry)
from command import (QuitCommand, RestockCommand, DispenseCommand)
from config.constants import COMMAND_LIST

class CommandProcessor:
    def __init__(self, inventory, menu, dispenser):
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser

        self.context = CommandContext(inventory, menu, dispenser)

        # Setup command registry
        self.registry = CommandRegistry()
        self.registry.register(COMMAND_LIST.get("quit"), QuitCommand())
        self.registry.register(COMMAND_LIST.get("restock"), RestockCommand())
        [self.registry.register(str(key), DispenseCommand()) for key in self.menu.id_to_drink.keys()]
        

    def process(self, command: str):
        command = command.strip().lower()
        if not command:
            return
        try:

            commandObj = self.registry.get(command)

            if not commandObj:
                raise InvalidCommandException(command)
            if command.isdigit():
                args = self.menu.id_to_drink[(command)]
            else:
                args = command
            commandObj.execute(args, self.context)
        except Exception as e:
            print(Fore.RED + str(e))
            print()
