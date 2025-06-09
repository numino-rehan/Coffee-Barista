from typing import Dict, Optional

from command_core import BaseCommand
from utils.loger_config import setup_logger

logger = setup_logger("registry_command")


class CommandRegistry:
    """
    Registry to store and retrieve command objects by keyword.

    Attributes:
        commands (Dict[str, BaseCommand]): A mapping from command keywords to command instances.
    """

    def __init__(self) -> None:
        """Initialize an empty command registry."""
        self.commands: Dict[str, BaseCommand] = {}

    def register(self, keyword: str, command_obj: BaseCommand) -> None:
        """
        Register a command object under a given keyword.

        Args:
            keyword (str): The command keyword.
            command_obj (BaseCommand): The command object instance.
        """
        self.commands[keyword] = command_obj
        logger.info(
            f"Registered command '{keyword}' with {command_obj.__class__.__name__}")

    def get(self, keyword: str) -> Optional[BaseCommand]:
        """
        Retrieve a registered command object by keyword.

        Args:
            keyword (str): The command keyword to look up.

        Returns:
            The command object if found, else None.
        """
        cmd = self.commands.get(keyword)
        if cmd:
            logger.debug(
                f"Found command '{keyword}': {cmd.__class__.__name__}")
        else:
            logger.warning(f"Command '{keyword}' not found in registry.")
        return cmd
