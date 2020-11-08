
class Report:
    def __init__(self, options):
        self.elapsed = 0
        self.total_errors = 0
        self.total_files = 0
        self.total_lines = 0
        self.messages = []

    def add_report(self, message):
        self.messages.append([message])