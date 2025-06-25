from typing import Dict, Optional

from command_core import BaseCommand
from utils import log_and_handle_errors, setup_logger

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
        logger.debug("Initialized CommandRegistry with empty command map.")

    @log_and_handle_errors("Error registering command")
    def register(self, keyword: str, command_obj: BaseCommand) -> None:
        """
        Register a command object under a given keyword.

        Args:
            keyword (str): The command keyword.
            command_obj (BaseCommand): The command object instance.
        """
        if keyword in self.commands:
            logger.warning(
                f"Overwriting existing command for keyword '{keyword}'."
            )

        self.commands[keyword] = command_obj
        logger.info(
            f"Registered command '{keyword}' -> {command_obj.__class__.__name__}"
        )

    @log_and_handle_errors("Error retrieving command")
    def get(self, keyword: str) -> Optional[BaseCommand]:
        """
        Retrieve a registered command object by keyword.

        Args:
            keyword (str): The command keyword to look up.

        Returns:
            Optional[BaseCommand]: The command object if found, else None.
        """
        cmd = self.commands.get(keyword)
        if cmd:
            logger.debug(
                f"Retrieved command for keyword '{keyword}': {cmd.__class__.__name__}"
            )
        else:
            logger.warning(f"No command found for keyword: '{keyword}'")
        return cmd
