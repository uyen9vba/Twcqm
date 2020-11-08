
import static.language


class Checker:
    def __init__(self, filename='stdin', lines=None, options=None, report=None, **kwargs):
        self.options = options
        self.indent_char = None
        self.line = None
        self.lines = []
        self.analyses = []

        if options is None:
            options = Style(kwargs).options
        else:
            assert not kwargs

    def read_line(self):
        if self.line >= len(self.lines):
            return ''

        line = self.lines[self.line]
        self.line += 1

        if self.indent_char is None and line[:1] in language.WHITESPACE:
            self.indent_char = line[0]

        return line

    def read_lines(file):
        if sys.version_info < (3,):
            try:
                with open(file, 'rU') as a:
                    return a.readlines()
        else:
            try:
                with open(file, 'rb') as a:
                    (encoding, lines) = tokenize.detect_encoding(a.readline)
                    a = io.TextIOWrapper(a, encoding, line_buffering=True)

                    return [line.decode(encoding) for line in lines] + a.readlines()

            except (LookupError, SyntaxError, UnicodeError):
                with open(file, encoding='latin-1') as a:
                    return a.readlines()

    def check_physical(self, line):
        for name, check, args in self.options.physical_checks:

