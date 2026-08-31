"""
Description:
coding in today's class;

simple expressions: literals, operators, and precedance
lecture example: PMDAS (no exponential) expressions

pipeline: tokenizer -> parser -> evaluator -> result

tokenizer:     (for PMDAS example)
    Identifies integers and floats, +-*/%, parentheses (), excluded text / comments

"""

from typing import Any


def eval(statement: Any):
    # checking the statement uses valid tokens
    for t in statement: # t for token
        assert t in "-0123456789"
    
def test_eval():
    pass
if __name__ == "__main__":
    test_eval()
    print("Done.")
