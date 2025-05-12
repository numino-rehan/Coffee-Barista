import sys
from command_core import BaseCommand

class QuitCommand(BaseCommand):
    def execute(self, args, context):
        sys.exit()
