class Handle():
    def __init__(self):
        self.global_function = {}

    def register_function(self, name, func):
        self.global_function[name] = func

    def get_function(self, name):
        return self.global_function.get(name)


handle = Handle()
