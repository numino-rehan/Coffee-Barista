from typing import Optional

from exceptions import InvalidCommandException
from command_core import CommandContext, CommandRegistry
from command import QuitCommand, RestockCommand, DispenseCommand
from config.constants import COMMAND_LIST
from utils import setup_logger, log_execution
from models import Inventory, Menu, Dispenser

logger = setup_logger("command_processor")


class CommandProcessor:
    """
    Processes user commands by delegating them to registered command handlers.

    Attributes:
        inventory (Inventory): Inventory instance managing ingredients.
        menu (Menu): Menu instance providing drink options.
        dispenser (Dispenser): Dispenser instance to dispense drinks.
        context (CommandContext): Shared command context containing inventory, menu, and dispenser.
        registry (CommandRegistry): Registry mapping command keywords to command objects.
    """

    def __init__(self) -> None:
        """
        Initialize the CommandProcessor with inventory, menu, and dispenser.

        Registers commands with the internal command registry.

        Args:
            inventory (Inventory): Inventory instance managing ingredients.
            menu (Menu): Menu instance providing drink options.
            dispenser (Dispenser): Dispenser instance to dispense drinks.
        """
        self.inventory = Inventory()
        self.menu = Menu(self.inventory)
        self.dispenser = Dispenser(self.inventory)

        self.context: CommandContext = CommandContext(
            self.inventory, self. menu, self.dispenser)

        self.registry: CommandRegistry = CommandRegistry()

        quit_cmd = COMMAND_LIST.get("quit")
        if quit_cmd is not None:
            self.registry.register(quit_cmd, QuitCommand())
        else:
            logger.error("QUIT command not found in COMMAND_LIST")

        restock_cmd = COMMAND_LIST.get("restock")
        if restock_cmd is not None:
            self.registry.register(restock_cmd, RestockCommand())
        else:
            logger.error("RESTOCK command not found in COMMAND_LIST")

        # Register dispense commands using drink IDs (strings)
        for key in self.menu.id_to_drink.keys():
            self.registry.register(str(key), DispenseCommand())

        logger.info("CommandProcessor initialized with commands registered.")

    @log_execution
    def process(self, command: str) -> None:
        """
        Process the given command string by looking it up and executing
        the associated command object.

        Args:
            command (str): The user input command.

        Raises:
            InvalidCommandException: If the command is not recognized.
            Exception: Any exception raised by command execution is propagated.
        """
        command = command.strip().lower()
        logger.info(f"Received command: '{command}'")

        if not command:
            logger.warning("Empty command received; ignoring.")
            return

        command_obj: Optional[object] = self.registry.get(command)
        if not command_obj:
            raise InvalidCommandException(command)

        # For numeric commands, map to drink name, else use the command itself as argument
        if command.isdigit() and command in self.menu.id_to_drink:
            args = self.menu.id_to_drink[command]
            logger.debug(f"Command is digit. Mapped args: '{args}'")
        else:
            args = command
            logger.debug(f"Command args: '{args}'")

        logger.info(f"Executing command '{command}' with args '{args}'")
        try:
            command_obj.execute(args, self.context)
            logger.info(f"Command '{command}' executed successfully.")
        except Exception as e:
            logger.error(f"Error executing command '{command}': {e}")
            raise

    def list_commands(self) -> list[str]:
        """
        Return a list of registered command keywords.

        Returns:
            list[str]: List of command strings registered.
        """
        return list(self.registry.commands.keys())
