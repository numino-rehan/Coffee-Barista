from typing import Optional

from exceptions import InvalidCommandException
from command_core import CommandContext, CommandRegistry
from command import QuitCommand, RestockCommand, DispenseCommand
from config.constants import COMMAND_LIST
from utils.decorators import log_execution
from utils.loger_config import setup_logger
from models import Inventory, Menu, Dispenser

logger = setup_logger("command_processor")


class CommandProcessor:
    """
    Processes user commands by delegating them to registered command handlers.

    Attributes:
        inventory: Inventory instance managing ingredients.
        menu: Menu instance providing drink options.
        dispenser: Dispenser instance to dispense drinks.
        context: Shared command context containing inventory, menu, and dispenser.
        registry: Registry mapping command keywords to command objects.
    """

    def __init__(self, inventory: Inventory, menu: Menu, dispenser: Dispenser) -> None:
        """
        Initialize the CommandProcessor with inventory, menu, and dispenser.

        Registers commands with the internal command registry.

        Args:
            inventory: Inventory instance managing ingredients.
            menu: Menu instance providing drink options.
            dispenser: Dispenser instance to dispense drinks.
        """
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser

        self.context: CommandContext = CommandContext(
            inventory, menu, dispenser)

        self.registry: CommandRegistry = CommandRegistry()
        self.registry.register(COMMAND_LIST.get("quit"), QuitCommand())
        self.registry.register(COMMAND_LIST.get("restock"), RestockCommand())
        for key in self.menu.id_to_drink.keys():
            self.registry.register(str(key), DispenseCommand())

        logger.info("CommandProcessor initialized with commands registered.")

    @log_execution
    def process(self, command: str) -> None:
        """
        Process the given command string.

        Args:
            command (str): The user input command.

        Raises:
            InvalidCommandException: If the command is not recognized.
        """
        command = command.strip().lower()
        logger.info(f"Received command: '{command}'")

        if not command:
            logger.warning("Empty command received; ignoring.")
            return

        command_obj: Optional[object] = self.registry.get(command)
        if not command_obj:
            raise InvalidCommandException(command)

        # Determine arguments to pass based on command type
        if command.isdigit():
            args: str = self.menu.id_to_drink[command]
            logger.debug(f"Command is digit. Mapped args: '{args}'")
        else:
            args = command
            logger.debug(f"Command args: '{args}'")

        logger.info(f"Executing command '{command}' with args '{args}'")
        command_obj.execute(args, self.context)
        logger.info(f"Command '{command}' executed successfully.")
