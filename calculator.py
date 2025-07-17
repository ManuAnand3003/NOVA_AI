#calculator.py

def evalualate_expression(expr):
    try:
        result=eval(expr)
        return f"The asnwer is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calcuate that. Error: {e}"