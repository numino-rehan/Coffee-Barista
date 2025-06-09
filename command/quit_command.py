import sys
from command_core import CommandContext, BaseCommand
from utils import setup_logger

logger = setup_logger("quit_command")


class QuitCommand(BaseCommand):
    """
    Command to quit/exit the coffee machine application.

    When executed, this command will terminate the program immediately.
    """

    def execute(self, args: str, context: CommandContext):
        """
        Execute the quit command.

        Args:
            args: Command arguments (unused).
            context: Shared command context (unused).

        Logs the quitting event and then exits the program.
        """
        logger.info("Executing quit command.")
        sys.exit()
        logger.info("Quit command executed successfully.")
