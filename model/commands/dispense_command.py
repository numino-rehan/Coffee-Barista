import sys
from .base_command import BaseCommand

class DispenseCommand(BaseCommand):
    def execute(self, args, context):
        context.dispenser.dispense(args)
        context.menu.refresh()