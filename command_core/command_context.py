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
        self.inventory = inventory
        self.menu = menu
        self.dispenser = dispenser

        logger.info(
            f"CommandContext initialized with: "
            f"Inventory={inventory.__class__.__name__}, "
            f"Menu={menu.__class__.__name__}, "
            f"Dispenser={dispenser.__class__.__name__}"
        )

    def __str__(self) -> str:
        return (
            f"CommandContext("
            f"inventory={self.inventory.__class__.__name__}, "
            f"menu={self.menu.__class__.__name__}, "
            f"dispenser={self.dispenser.__class__.__name__})"
        )
