class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, keyword, command_obj):
        self.commands[keyword] = command_obj

    def get(self, keyword):
        return self.commands.get(keyword)
