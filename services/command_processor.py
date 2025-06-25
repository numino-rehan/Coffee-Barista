from typing import Optional

from command import DispenseCommand, QuitCommand, RestockCommand
from command_core import CommandContext, CommandRegistry
from config.constants import COMMAND_LIST
from exceptions import InvalidCommandException
from models import Dispenser, Inventory, Menu
from utils import log_and_handle_errors, setup_logger

logger = setup_logger("command_processor")


class CommandProcessor:
    """
    Processes user commands by delegating them to registered command handlers.
    """

    def __init__(self) -> None:
        """
        Initialize the CommandProcessor with inventory, menu, and dispenser.

        Registers commands with the internal command registry.
        """
        self.inventory = Inventory()
        self.menu = Menu(self.inventory)
        self.dispenser = Dispenser(self.inventory)

        self.context = CommandContext(
            self.inventory, self.menu, self.dispenser)
        self.registry = CommandRegistry()

        quit_cmd = COMMAND_LIST.get("quit")
        if quit_cmd:
            self.registry.register(quit_cmd, QuitCommand())
        else:
            logger.error("QUIT command not found in COMMAND_LIST")

        restock_cmd = COMMAND_LIST.get("restock")
        if restock_cmd:
            self.registry.register(restock_cmd, RestockCommand())
        else:
            logger.error("RESTOCK command not found in COMMAND_LIST")

        for key in self.menu.id_to_drink:
            self.registry.register(str(key), DispenseCommand())

        logger.info("CommandProcessor initialized and commands registered.")

    @log_and_handle_errors("Error processing user command")
    def process(self, command: str) -> None:
        """
        Process the given command string by executing the appropriate command handler.

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
            raise InvalidCommandException(f"Unrecognized command: '{command}'")

        args = self.menu.id_to_drink[command] if command.isdigit(
        ) and command in self.menu.id_to_drink else command
        logger.debug(f"Command args resolved to: '{args}'")

        command_obj.execute(args, self.context)
        logger.info(f"Command '{command}' executed successfully.")

    def list_commands(self) -> list[str]:
        """
        Return a list of registered command keywords.

        Returns:
            list[str]: List of command strings registered.
        """
        return list(self.registry.commands.keys())
