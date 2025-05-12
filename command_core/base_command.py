class BaseCommand:
    def execute(self, args, context):
        raise NotImplementedError("Each command must implement the execute method.")
