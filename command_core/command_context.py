from models import Dispenser, Inventory, Menu
from utils import setup_logger

logger = setup_logger("command_context")


class CommandContext:
    """
    Holds shared components used by command objects.

    Attributes:
        inventory (Inventory): The inventory instance managing ingredient stocks.
        menu (Menu): The menu instance managing available drinks and pricing.
        dispenser (Dispenser): The dispenser instance handling drink dispensing.
    """

    def __init__(self, inventory: Inventory, menu: Menu, dispenser: Dispenser):
        """
        Initialize the CommandContext with inventory, menu, and dispenser.

        Args:
            inventory (Inventory): Inventory instance.
            menu (Menu): Menu instance.
            dispenser (Dispenser): Dispenser instance.
        """
        logger.info("Initializing CommandContext with inventory, menu, and dispenser.")
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser
