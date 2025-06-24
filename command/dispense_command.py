from colorama import Fore, Style, init

from command_core import BaseCommand, CommandContext
from utils import setup_logger

init(autoreset=True)  # Automatically reset colors after each print

logger = setup_logger("dispense_command")


class DispenseCommand(BaseCommand):
    """
    Command to dispense a drink from the coffee machine.

    This command uses the dispenser component to dispense the requested drink,
    and then refreshes the menu to update availability based on inventory changes.
    """

    def execute(self, args: str, context: CommandContext):
        """
        Execute the dispense command.

        Args:
            args (str): The name of the drink to dispense.
            context (CommandContext): The shared context containing inventory, menu, and dispenser.

        Logs the action and refreshes the menu after dispensing.
        Prints colored user notifications.
        """
        logger.info(f"Executing dispense command for: {args}")
        print(f"{Fore.CYAN}Dispensing drink: {args}...{Style.RESET_ALL}\n")

        context.dispenser.dispense(args)
        context.menu.refresh()

        logger.info("Dispense command executed successfully.")
        print(f"{Fore.GREEN}Drink dispensed successfully.{Style.RESET_ALL}\n")
