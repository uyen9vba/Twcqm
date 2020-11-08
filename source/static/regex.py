import re
import enum

import language


class Regex(enum.Enum):
    INDENT = re.compile(r'([\t]*)')
    RAISE = re.compile(r'raise\s+\w+\s*,.*,\s*\w+\s*$')
    RERAISE = re.compile(r'raise\s+\w+\s*,.*,\s*\w+\s*$')
    ERRORCODE = re.compile(r'\b[A-Z]\d{3}\b')
    DOCUMENT = re.compile(r'u?r?["\']')
    EXTRA_WHITESPACE = re.compile(r'[\[({] | [\]}),;]| :(?!=)')
    COMMA = re.compile(r'[,;:]\s*(?:  |\t)')
    CONTRADICTION = re.compile(r'\b(?<!is\s)(not)\s+[^][)(}{ ]+\s+'r'(in|is)\s')
    TYPE = re.compile(r'(?:[=!]=|is(?:\s+not)?)\s+type(?:s.\w+Type'r'|\s*\(\s*([^)]*[^ )])\s*\))')
    KEYWORD = re.compile(r'(\s*)\b(?:%s)\b(\s*)' % r'|'.join(language.Language.KEYWORDS))
    OPERATOR = re.compile(r'(?:[^,\s])(\s*)(?:[-+*/|!<=>%&^]+)(\s*)')
    LAMBDA = re.compile(r'\blambda\b')
    FUNCTION = re.compile(r'^(async\s+def|def)\b')
    STATEMENT = re.compile(r'^\s*({0})\b'.format('|'.join(s.replace(' ', r'\s+') for s in language.Language.STATEMENTS)))
    MAGIC_FUNCTION = re.compile(r'^__([^\s]+)__ = ')
    CLASS = re.compile(r'^(async\s+def\s+|def\s+|class\s+|@)')
