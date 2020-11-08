
import keyword
import tokenize
import enum


class Language(enum.Enum):
    KEYWORDS = frozenset(keyword.kwlist + ["print", "async"])
    STATEMENTS = frozenset(['def', 'async def', 'for', 'async for', 'if',
                            'elif', 'else', 'try', 'except', 'finally',
                            'with', 'async with', 'class', 'while'])
    UNARY_OPERATORS = frozenset([">>", "**", "*", "+", "-"])
    ARITHMETIC_OPERATORS = frozenset(["**", "*", "/", "//", "+", "-", "@"])
    WHITESPACE = frozenset("\t")
    NEWLINE = frozenset([tokenize.NL, tokenize.NEWLINE])
    NON_WHITESPACE_OPERATORS = frozenset(['^', '&', '|', '<<', '>>', '%'])
    WHITESPACE_OPERATORS = frozenset(['**=', '*=', '/=', '//=', '+=', '-=', '!=', '<>',
                                    '<', '>', '%=', '^=', '&=', '|=', '==', '<=', '>=',
                                    '<<=', '>>=', '=', 'and', 'in', 'is', 'or', '->', ':='])
    SKIP_TOKENS = NEWLINE.union([tokenize.INDENT, tokenize.DEDENT])
