
import time


class Report:
    def __init__(self):
        self.path = ''
        self.analyses_time = 0
        self.file_errors = 0
        self.total_errors = 0
        self.total_files = 0
        self.total_lines = 0
        self.plain_messages = {}
        self.print_messages = []
        self.counts = {'directories': 0, 'files': 0, 'logical lines': 0, 'physical lines': 0}

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
            print(f'{path}:{row}:{column}: {code} {message}')

        return self.file_errors

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.analyses_time = time.time() - self.start_time
