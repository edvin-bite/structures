"""
Description:


Notes:
language is associating something (tokens) with meaning, 
    
"""

from typing import Any


def eval(statement: Any):
    # checking the statement uses valid tokens
    for t in statement: # t for token
        assert t in "0123456789"

def test_eval():
    pass
if __name__ == "__main__":
    test_eval()
    print("Done.")
