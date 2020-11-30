
import os
import fnmatch

import report


class Options:
    def __init__(self, report=report.Report(), *args, **kwargs):
        self.argv = kwargs.pop('argv', False)
        self.config = kwargs.pop('config', False)'''
        self.parser = kwargs.pop('parser', None)
        self.verbose = kwargs.pop('verbose', None)

        self.config = dict(*args, **kwargs)
        self.exclude_files = str.split(self.config.get('exclude_files'))

        self.args = None if argv else config.get('paths', None)

        self.report = report'''
'''
    def check_paths(self, paths=None):
        if paths is None:
            paths = self.config.get('paths', None)

        try:
            for a in paths:
                if os.path.isdir(path):
                    self.'''
'''
    def run_analysis(self, filename, lines=None, expected=None, line_offset=0):
        if self.verbose:
            print(f'checking {filename}')
            '''
'''
    def find_files(self, dirname):
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
                if any(fnmatch(a, self.exclude_files)) and
                not self.check_exclusion(a, dirpath):
                    #'''

    def check_exclusion(self, filename, parent=None):
        if not self.config.exclude:
            return False

        if any(fnmatch(os.path.basename(filename), a) for a in self.exclude_files):
            return True

        if parent:
            filename = os.path.join(parent, filename)

        filename = os.path.abspath(filename)

        return any(fnmatch(filename, self.exclude_files))
