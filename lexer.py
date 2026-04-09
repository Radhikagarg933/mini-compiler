import re

KEYWORDS = {"show", "print", "if", "else", "end", "while", "for", "switch", "case", "input"}
OPERATORS = {"is", "➕", "➖", "✖️", "✖", "➗", "🔺", "🔻", "🤝"}

token_specification = [
    ('NUMBER',   r'-?\d+(\.\d+)?'),
    ('OPERATOR', r'is|➕|➖|✖️|✖|➗|🔺|🔻|🤝'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COMMA',    r','),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def tokenize(line):
    """Return list of raw tokens (no formatting)"""
    tokens = []

    for mo in re.finditer(tok_regex, line):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'SKIP':
            continue
        elif kind == 'IDENTIFIER' and value in KEYWORDS:
            tokens.append(value)  # Keep keywords as-is
        elif kind == 'IDENTIFIER' and value in OPERATORS:
            tokens.append(value)  # Keep operators as-is
        else:
            tokens.append(value)

    return tokens
