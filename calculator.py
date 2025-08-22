#calculator.py
from simpleeval import simple_eval

def evaluate_expression(expr):
    try:
        result = simple_eval(expr)
        return f"The answer is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calculate that. Error: {e}"