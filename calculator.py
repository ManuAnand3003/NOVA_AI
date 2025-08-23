#calculator.py
from simpleeval import simple_eval

import re
import math

def evaluate_expression(expr):
    expr = expr.lower().strip()
    # Handle cube, square, square root, etc.
    cube_match = re.match(r"cube of (\d+)", expr)
    if cube_match:
        num = int(cube_match.group(1))
        return f"The answer is {num ** 3}"

    square_match = re.match(r"square of (\d+)", expr)
    if square_match:
        num = int(square_match.group(1))
        return f"The answer is {num ** 2}"

    sqrt_match = re.match(r"square root of (\d+)", expr)
    if sqrt_match:
        num = int(sqrt_match.group(1))
        return f"The answer is {math.sqrt(num)}"

    # Fallback to simple_eval for direct math expressions
    try:
        result = simple_eval(expr)
        return f"The answer is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calculate that. Error: {e}"