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
    (r"\+", "addition"),
    (r"\-", "subtraction"),
    (r"\*", "multiplication"),
    (r"\/", "division"),
   #(r"\%", ""),
    (r"\(", "open_par"),
    (r"\)", "close_par"),
]

patterns = [(re.compile(p), tag) for p, tag in patterns] # I hate python

# print(patterns) 

def tokenize(chars: str):
    """
    Tokenizes a string for use by the parser. matches patterns with token tags needed by the parser for syntatic step

    Args:
        chars (_type_): _description_
    """
    tokens = []
    position = 0
    line = 1
    column = 1
    cur_tag = None
    # Pylance really does not like his stylistic choices. so much use of side effects.
    while position < len(chars):
        for pattern , tag in patterns:
            match = pattern.match(chars, position)
            if match:
                cur_tag = tag
                break
        assert match is not None
        value = match.group(0)
        
        if cur_tag == "error":
            raise Exception(f"unexpected character: {value!r}")
        
        if cur_tag != "whitespace":
            token = {"tag": cur_tag, "line":line,"column":column }
            if cur_tag == "number":
                token["value"] = int(value)
            tokens.append(token)
        
        for ch in value:
            if ch == "\n":
                line += 1
                column = 1
            else:
                column += 1
        
        position = match.end()
        # print(value)
        # print(cur_tag)
        # print()
    tokens.append({"tag": None, "line": line, "column": column})
    return tokens
        

def test():
    print("test general:\n")
    try:
        tokenize("145 + 3 - 48")
    except Exception as e:
        print("error...")

if __name__=="__main__":
    test()
    print("done")