"""
Description:


Notes:
language is associating something (tokens) with meaning, 
    
"""

from typing import Any


def eval(statement: Any):
    # checking the statement uses valid tokens
    for t in statement:
        assert t in "0123456789"
    pass
if __name__ == "__main__":
    pass
