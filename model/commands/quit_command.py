import sys
from .base_command import BaseCommand

class QuitCommand(BaseCommand):
    def execute(self, args, context):
        sys.exit()
