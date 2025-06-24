from abc import ABC, abstractmethod

from command_core.command_context import CommandContext
from utils import setup_logger

logger = setup_logger("base_command")


class BaseCommand(ABC):
    """
    Abstract base class for all commands.
    """

    @abstractmethod
    def execute(self, args: str, context: CommandContext) -> None:
        """
        Execute the command with given arguments and context.

        Args:
            args: Arguments required to execute the command (type varies per command).
            context: Shared context object containing relevant state and components.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        logger.error(
            f"Execute method not implemented in {self.__class__.__name__}")
        raise NotImplementedError(
            "Each command must implement the execute method.")
