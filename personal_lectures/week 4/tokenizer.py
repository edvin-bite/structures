"""
"homework": try out and see how things are ordered
Tokenizer

uses JSON for AST tree for class example
smaller binary alternative for python: bison? bithon?

Give set of local patterns to scan for.  EBNF below:
# Pattern strategy:     [ {} optional? | ]
    expression = term { ("+" | "-") term }              // expression, term, and factor in this example are meaningless, they seperate *precedance*
    term       = factor { ("*" | "/") factor }    // this is recursive descent.
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
    (r".", "error"),
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
            raise Exception(f"Unexpected character: {value!r}")
        
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
        
###### Tests ######

def test():
    print("test general:\n")
    try:
        tokenize("145 + 3 - 48")
    except Exception as e:
        print("error...")


def test_digits():
    print("test tokenize digits")
    t = tokenize("123")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 123
    assert t[1]["tag"] is None
    t = tokenize("1")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 1
    assert t[1]["tag"] is None


def test_operators():
    print("test tokenize operators")
    t = tokenize("+ - * / ( )")
    tags = [token["tag"] for token in t]
    assert tags == ["+", "-", "*", "/", "(", ")", None]


def test_expressions():
    print("test tokenize expressions")
    t = tokenize("1+222*3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 222
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None


def test_whitespace():
    print("test tokenize whitespace")
    t = tokenize("1 +\t2  \n*    3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 2
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None


def test_error():
    print("test tokenize error")
    try:
        tokenize("1@@@ +\t2  \n*    3")
    except Exception as e:
        assert str(e) == "Unexpected character: '@'"
        return
    raise Exception("Error did not happen.")


if __name__ == "__main__":
    # test()
    test_digits()
    test_operators()
    test_expressions()
    test_whitespace()
    test_error()
    print("done.")
