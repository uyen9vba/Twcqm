
import tokenize

import static.language
import report


class Analyzer:
    def __init__(self, filename=None, lines=None):
        self.filename = filename
        self.lines = lines
        self.indent_char = None
        self.line_number = 0
        self.line_count = 0
        self.physical_analyses = []
        self.logical_analyses = []
        self.report = report.Report()
        
        self.argv = kwargs.pop('argv', False)
        self.verbose = kwargs.pop('verbose', None)

        self.config = dict(*args, **kwargs)
        self.args = None if self.argv else config.get('paths', None)

    def run_analyses(self, paths=None):
        if paths is None:
            paths = self.config.get('paths', None)

        self.report.start_timer()

        try:
            for a in paths:
                if os.path.isdir(path):
                    self.run_analyses_on_directory(a)
                elif not self.check_exclusion(a):
                    self.run_analyses_on_file(a)
        except KeyboardInterrupt:
            print('stopped analyses')

        self.report.stop_timer()

        return report

    def add_physical_analysis(column, message=None):
        self.pysical_analyses.append([column, message])

    def add_logical_analysis(column, message=None):
        self.logical_analyses.append([column, message])

    def read_line(self):
        if self.line_number >= len(self.lines):
            return ''

        line = self.lines[self.line_number]
        self.line_number += 1

        if self.indent_char is None and line[:1] in language.WHITESPACE:
            self.indent_char = line[0]

        return line

    def read_lines(filename):
        try:
            with open(filename, 'rb') as a:
                (encoding, lines) = tokenize.detect_encoding(a.readline)
                a = io.TextIOWrapper(a, encoding, line_buffering=True)

                return [line.decode(encoding) for line in lines] + a.readlines()
        except (LookupError, SyntaxError, UnicodeError):
            with open(file, encoding='latin-1') as a:
                return a.readlines()

    def run_physical_analyses(self, line):
        for name, analysis, args in self.physical_analyses:
            result = self.run_analysis(analysis, args)

            if result is not None:
                (column, message) = result

                if message[:4] == 'E101':
                    self.indent_char = line[0]

    def run_analyses_on_directory(self, dirname):
        if not self.check_exclusion(dirname.rstrip('/')):
            return

        for dirpath, dirnames, filenames in os.walk(dirname):
            if self.verbose:
                print('directory ' + dirpath)

            self.report.counts['directories'] += 1

            for a in sorted(dirnames):
                if self.check_exclusion(a, dirpath):
                    dirnames.remove(a)

            for a in sorted(filenames):
                if any(fnmatch(a, self.exclude_files)) and not self.check_exclusion(a, dirpath):
                    self.run_analyses_on_file(os.path.join(dirpath, a))

    def run_analysis(self, analysis, args_names):
        args = []

        for a in args:
            args.append(getattr(self, name))

        return analysis(*arguments)

    def run_analyses_on_file(self, filename):
        if self.verbose:
            print(f'checking {filename}')

        tokens = []

        for a in self.generate_tokens():
            tokens.append(a)
            type, text = a[0:2]
            nesting = 0

            if self.options.verbose >= 3:
                if a[2][0] == a[3][0]:
                    pos = f'[{a[2][1]}:{a[3][1]}]'
                else:
                    pos = f'l.{a[3][0]}'
                
                print(f'l.{a[2][0]}' + '\t' + pos +  '\t' + tokenize.tok_name[a[0]] + '\t' + text)
            
            if type == tokenize.OP:
                if text in '([{':
                    nesting += 1
                elif text in '}])':
                    nesting -= 1
            elif not nesting:
                if type in language.Language.NEWLINE:
                    if type == tokenize.NEWLINE:
                        self.run_logical_analyses(tokens)
                        self.blank_before = 0
                    elif len(tokens) == 1:
                        del self.tokens[0]
                    else:
                        self.run_logical_analyses(tokens)

        if tokens:
            self.run_physical_analyses(self.lines[-1])
            self.run_logical_analyses(tokens)

        return self.report.get_file_results()


    def run_logical_analyses(self, tokens):
        self.line_count += 1
        mapping = self.build_line(tokens)

        if not mapping:
            return None

    def build_line(self, tokens):
        logical = []
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
                   previous_text = self.lines[previous_row - 1][previous_column - 1]

                   if previous_text == ',' or (previous_text not in '{[(' and text not in '}])'):
                       text = ' ' + text
                elif previous_column != column:
                    text = line[previous_column:column] + text

            logical.append(text)
            length += len(text)
            mapping.append((length, end))
            (previous_row, previous_column) = end

        self.line = ''.join(logical)
        
        return mapping
            

    def generate_tokens(self):
        try:
            for a in tokenize.generate_tokens(self.readline):
                if a[2][0] > len(self.lines):
                    return
                yield a
        except (SyntaxError, tokenize.TokenError):
            report.Report.add_report('E902')

    def check_exclusion(self, filename, parent=None):
        if not self.config.exclude:
            return False

        if any(fnmatch(os.path.basename(filename), a) for a in self.exclude_files):
            return True

        if parent:
            filename = os.path.join(parent, filename)

        filename = os.path.abspath(filename)

        return any(fnmatch(filename, self.exclude_files))
