from command_core import BaseCommand

class RestockCommand(BaseCommand):
    def execute(self, args, context):
        context.inventory.restock()
        context.menu.refresh()
