
import regex
import language


analyses = []


def add_analysis(column, code=None):
    analyses.append([column, code])


@add_analysis
def indent(line, indent):
    # E101
    # W191
    search = regex.Regex.INDENT.match(line).group(1)

    for column, char in enumerate(search):
        if char != indent:
            return column, "E101 Indentation contains tabs and whitespaces"

    if '\t' in search:
        return search.index('\t'), "W191 Indentation contains tabs"


def trailing_whitespace(line):
    # W291
    # W293
    line = line.rstrip('\n')
    line = line.rstrip('\r')
    line = line.rstrip('\x0c')

    if line != (a := line.rstrip(' \t\v')):
        if a:
            return len(a), "W291 Trailing whitespace"
        else:
            return 0, "W293 Blank line contains whitespace"


def trailing_blank_lines(line, lines, line_number, total_lines):
    # W391
    # W292
    if line_number == total_lines:
        a = line.rstrip('\r\n')

        if line and not a:
            return 0, "W391 Blank line at end of file"

        if line == a:
            return len(lines[-1]), "W292 No newline at end of file"


def extra_whitespace(line):
    # E201
    for a in regex.Regex.EXTRA_WHITESPACE.finditer(line):
        text = a.group()
        char = text.strip()

        if text == char + ' ':
            yield a.start() + 1, f"E201 Whitespace after {char}"
        elif line[a.start() - 1] != ',':
            code = ('E202' if char in '}])' else 'E203')
            yield a.start(), f"{code} whitespace before '{char}'"


def keyword_whitespace(line):
    # E274
    # E272
    # E273
    # E271
    # E275
    if line.startwith('from '):

        if -1 < (a := line.find('from ')):
            column = a + len('from ') - 1
            yield column, "E275 Missing whitespace after keyword"

    for a in regex.Regex.KEYWORD.finditer(line):
        before, after = a.groups()

        if '\t' in before:
            yield a.start(1), "E274 Tab before keyword"
        elif len(before) > 1:
            yield a.start(1), "E272 Multiple spaces before keyword"

        if '\t' in after:
            yield a.start(2), "E273 Tab after keyword"
        elif len(after) > 1:
            yield a.start(2), "E271 Multiple spaces after keyword"


def missing_whitespace(line):
    # E231
    for a in range(len(line) - 1):
        char = line[a]

        if char in ',;:' and line[a + 1] not in language.Language.WHITESPACE:

            if char == ':' and line[:a].count('[') > line[:a].count(']') and \ 
            line[:a].rfind('{') < line[:a].rfind('['):
                continue
            elif char == ',' and line[:a] == ')':
                continue
            elif char == ':' and line[:a] == '=':
                continue
            else:
                yield a, f"E231 Missing whitespace after {char}"


"""
def parameter_whitespace(line, tokens):
    # E211
    for a in range(1, len(tokens)):
"""


def operator_whitespace(line):
    # E221
    # E222
    # E223
    # E224
    for a in regex.Regex.OPERATOR.finditer(line):
        before, after = a.groups()

        if '\t' in before:
            yield a.start(1), "E223 Tab before operator"
        elif len(before) > 1:
            yield a.start(1), "E221 Multiple spaces before operator"

        if '\t' in after:
            yield a.start(2), "E224 Tab after operator"
        elif len(after) > 1:
            yield a.start(2), "E222 Multiple spaces after operator"


def comma_whitespace(line):
    # E241
    # E242
    for a in regex.Regex.COMMA.finditer(line):

        if '\t' in a.group():
            yield a.start() + 1, f"E242 Tab after '{a.group()[0]}'"
        else:
            yield a.start() + 1, f"E241 Multiple spaces after '{a.group()[0]}'"