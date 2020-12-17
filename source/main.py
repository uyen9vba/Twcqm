#!/usr/bin/env python3

import signal
import os
import configparser
import sys

import utilities
import analyzer

def main(*args, *kwargs):
    config = configparser.ConfigParser()

    config_path = config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'),
            encoding='utf-8')

    args = utilities.parse_args(config)

    if not config_path:
        print('Config path missing or invalid')
        sys.exit(0)

    analyzer_ = analyzer.Analyzer(argv=True)

    report = analyzer_.run_analyses()

if __name__ == '__main__':
    main()
