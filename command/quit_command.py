import sys

from colorama import Fore, Style, init

from command_core import BaseCommand, CommandContext
from utils import setup_logger

init(autoreset=True)

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

        Logs the quitting event and then exits the program with user notification.
        """
        logger.info("Executing quit command.")
        print(f"{Fore.YELLOW}Exiting the coffee machine. Goodbye!{Style.RESET_ALL}")
        sys.exit()
