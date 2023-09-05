import math

def calculate(expression):
    try:
        # Ensure mathematical functions like 'sqrt' are recognized
        safe_dict = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e
        }

        # Evaluate the expression using eval() and the safe_dict
        result = eval(expression, safe_dict)

        return result
    except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
        return f'Error: {e}'


expression = input("Enter an expression: ")
result = calculate(expression)
print("Result:", result)
