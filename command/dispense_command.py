from command_core import CommandContext, BaseCommand
from utils.loger_config import setup_logger

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
        """
        logger.info(f"Executing dispense command for: {args}")
        context.dispenser.dispense(args)
        context.menu.refresh()
        logger.info("Dispense command executed successfully.")
