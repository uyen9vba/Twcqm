
import os
import fnmatch


class Options:
    def __init__(self, *args, **kwargs):
        argv = kwargs.pop('argv', False)
        config = kwargs.pop('config', False)
        parser = kwargs.pop('parser', None)
        verbose = kwargs.pop('verbose', None)

        config = dict(*args, **kwargs)
        exclude_files = str.split(config.get('exclude_files'))

        args = None if argv else config.get('paths', None)

    def run_analyses(self, paths=None):
        if paths is None:
            paths = self.config.get('paths', None)

        try:
            for a in paths:
                if os.path.isdir(path):
                    self.#

    def run_analysis(self, filename, lines=None, expected=None, line_offset=0):
        if self.verbose:
            print(f'checking {filename}')
            #

    def find_files(self, dirname):
        dirname = dirname.rstrip('/')

        if not self.check_exclusion(dir):
            return

        for dirpath, dirnames, filenames in os.walk(dirname):
            if self.verbose:
                print('directory ' + dirpath)

            for a in sorted(dirnames):
                if self.check_exclusion(a, dirpath):
                    dirnames.remove(a)

            for a in sorted(filenames):
                if any(fnmatch(a, self.exclude_files)) and
                not self.check_exclusion(a, dirpath):
                    self.#

    def check_exclusion(self, filename, parent=None):
        if not self.config.exclude:
            return False

        if any(fnmatch(os.path.basename(filename), a) for a in self.exclude_files):
            return True

        if parent:
            filename = os.path.join(parent, filename)

        filename = os.path.abspath(filename)

        return any(fnmatch(filename, self.exclude_files))