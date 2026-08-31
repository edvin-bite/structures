"""
Tokenizer

uses JSON for AST tree for class example
smaller binary alternative for python: bison? bithon?

Give set of local patterns to scan for. \/ EBNF
# Pattern strategy:     [ {} optional? | ]
    expression = term { ("+" | "-") term }              // expression, term, and factor in this example are meaningless, they seperate *precedance*
    term       = factor { ("*" | "/" | "%") factor }    // this is recursive descent.
    factor     = <number> | "(" expression ")"            // "+" and "-" are terminal, operator? <> means terminal in EBNF
"""

import re


patterns = [
    (r"\d+", "number"), # '\d' for ascii digit & '+' for regex to match any number of preceding regex to the tag
    (r"\s+", "whitespace"), # '\s' is ascii whitespace/space
    (r"\+", "+"),
    (r"\-", "-"),
    (r"\*", "*"),
    (r"\/", "/"),
   #(r"\%", ""),
    (r"\(", "("),
    (r"\)", ")"),
]

patterns = [(re.compile(p), tag) for p, tag in patterns] # I hate python

def tokenize(chars):
    """
    Tokenizes a string for use by the parser. matches patterns with token tags needed by the parser for syntatic step

    Args:
        chars (_type_): _description_
    """
    tokens = []
    