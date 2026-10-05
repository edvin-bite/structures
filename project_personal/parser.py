import re

patterns = [
    # Nothings
    (r"\s+", "whitespace"),
    (r"//[^\r\n]*", "comment"),
    # types
    (r'"(?:\\[\r\n]|[^"\\\r\r])*"', "string"),
    (r"\d*\.\d+|\d+\.\d|\d+", "number"),
]