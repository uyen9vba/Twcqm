
from static.language import Language

class Report:
    def __init__(self, options):
        self.path = ''
        self.elapsed = 0
        self.file_errors = 0
        self.total_errors = 0
        self.total_files = 0
        self.total_lines = 0
        self.plain_messages = {}
        self.print_messages = []
        self.counts = {'directories': 0, 'files': 0, 'logical lines': 0, 'physical lines': 0}
        self.report_format = f'{path}:{row}:{column}: {code} {message}'

    def add_error(self, row, column, message, analysis):
        code = message[:4]

        if code in self.counts:
            self.counts[code] += 1
        else:
            self.counts[code] = 1
            self.messages[code] = text[5:]

        self.total_errors += 1

        if code and self.count[code] == 1:
            self.print_messages.append((row, column, code, message[5:]))
        
        return code

    def get_file_results(self):
        path = self.path

        for row, column, code, message in self.print_messages:
            print(self.report_format)

        return self.file_errors
