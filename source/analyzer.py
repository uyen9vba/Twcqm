
import tokenize

import static.language
import report


class Analyzer:
    def __init__(self, lines, options=Style(kwargs).options, **kwargs):
        self.options = options
        self.indent_char = None
        self.line = None
        self.lines = lines
        self.physical_analyses = []
        self.logical_analyses = []

    def add_physical_analysis(column, message=None):
        self.pysical_analyses.append([column, message])

    def add_logical_analysis(column, message=None):
        self.logical_analyses.append([column, message])

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

    def run_physical_analyses(self, line):
        for name, check, args in self.options.physical_checks:
            #

    def run_analyses(self, filename):
        tokens = []

        for a in self.generate_tokens():
            tokens.append(a)
            type, text = a[0:2]
            nesting = 0

            if self.options.verbose >= 3:
                if a[2][0] == a[3][0]:
                    pos = f'[{a[2][1] or ''}:{a[3][1]}]'
                else:
                    pos = f'l.{a[3][0]'
                
                print(f'l.{a[2][0]}' + '\t' + pos +  '\t' + tokenize.tok_name[a[0]] + '\t' + text)
            
            if type == tokenize.OP:
                if text in '([{':
                    nesting += 1
                elif text in '}])':
                    nesting -= 1
            elif not nesting:
                if type in language.Language.NEWLINE:
                    if type == tokenize.NEWLINE:
                        self.run_logical_analysis(tokens)

    def run_logical_analyses(self, tokens):
        #

    def build_line(self, tokens):
        logical = []
        comments = []
        previous_row = None
        previous_column = None

        for type, text, start, end, line in tokens:
            if type in language.Language.SKIP_TOKENS:
                continue
            
            if type == tokenize.COMMENT:
                comments.append(text)
                continue

            if previous_row:
                (row, column) = start

                if previous_row != row:
                    

            

    def generate_tokens(self):
        try:
            for a in tokenize.generate_tokens(self.readline):
                if a[2][0] > len(self.lines):
                    return
                yield a
        except (SyntaxError, tokenize.TokenError):
            report.Report.add_report('E902')
