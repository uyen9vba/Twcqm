
import argparse


def parse_args():
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '-v',
        '--verbose',
        default=0,
        action='count',
        help='print status messages or debug with -vv'
    )
    argument_parser.add_argument(
        '-q',
        '--quiet',
        default=0,
        action='count',
        help='report only file name or nothing -qq'
    )
    argument_parser.add_argument(
        '-r',
        '--repeat',
        default=True,
        action='store_true',
        help='(obsolete) show all occurrences of the same error'
    )
    argument_parser.add_argument(
        '--first',
        action='store_false',
        dest='repeat',
        help='show first occerrence of each error'
    )
    argument_parser.add_argument(
        '--exclude',
        metavar='patterns',
        default=DEFAULT_EXCLUDE,
        help='exclude files of directories which match these comma separated patterns (default: %default)'
    )
    argument_parser.add_argument(
        '--filename',
        metavar='patterns',
        default='*.py',
        help='when parsing directories, only check filenames matching these comma separated patterns (default: %default)'
    )
    argument_parser.add_argument(
        '--select',
        metavar='errors',
        default='',
        help='select errors and warnings (e.g. E,W6)'
    )
    argument_parser.add_argument(
        '--ignore',
        metavar='errors',
        default='',
        help='skip errors and warnings (e.g. E4,W) (default: %s)' %DEFAULT_IGNORE
    )
    argument_parser.add_argument(
        '--show-source',
        action='store_true',
        help='show source code for each error'
    )
    argument_parser.add_argument(
        '--show-pep8',
        action='store_true',
        help='show text of PEP8 for each error (implies --first)'
    )
    argument_parser.add_argument(
        '--statistics',
        action='store_true',
        help='count errors and warnings'
    )
    argument_parser.add_argument(
        '--count',
        action='store_true',
        help='print total number of errors and warnings to standard error and set exit code to 1 if total is not null'
    )
    argument_parser.add_argument(
        '--hang_closing',
        action='store_true',
        help='hang closing bracket instead of matching indentation of opening line of the bracket'
    )
    argument_parser.add_argument(
        '--format',
        metavar='format',
        default='default',
        help='set the error format [default|pylint|custom]'
    )
    argument_parser.add_argument(
        '--diff',
        action='store_true',
        help='report changes only within line number ranges in the unified diff received on STDIN'
    )
    args = argument_parser.parse_args()

    return args


def run_analyses(filename):
    