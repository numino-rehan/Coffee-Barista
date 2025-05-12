import sys
from command_core import BaseCommand

class DispenseCommand(BaseCommand):
    def execute(self, args, context):
        context.dispenser.dispense(args)
        context.menu.refresh()