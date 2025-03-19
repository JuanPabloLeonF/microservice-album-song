class ErrorSessionDatabase(Exception):
    def __init__(self, message):
        self.message = message

class IntegrityErrorDatabase(Exception):
    def __init__(self, message):
        self.message = message