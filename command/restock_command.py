from colorama import Fore, Style, init

from command_core import CommandContext, BaseCommand
from utils import setup_logger

init(autoreset=True)

logger = setup_logger("restock_command")


class RestockCommand(BaseCommand):
    """
    Command to restock all ingredients in the inventory.

    When executed, this command refills the inventory to maximum stock levels
    and refreshes the menu availability accordingly.
    """

    def execute(self, args: str, context: CommandContext):
        """
        Execute the restock command.

        Args:
            args: Command arguments (unused).
            context: Shared command context containing inventory and menu.

        Logs the restocking action and refreshes the menu afterward.
        Prints user notification about restock.
        """
        logger.info("Executing restock command.")
        context.inventory.restock()
        context.menu.refresh()
        logger.info("Restock command executed successfully.")
        print(
            f"{Fore.GREEN}Restocking completed. Inventory is now full.{Style.RESET_ALL}")
