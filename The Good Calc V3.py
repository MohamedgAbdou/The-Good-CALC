from sympy import *

def calculate(expression):
    try:
        parsed_expression = parse_expr(expression)
        result = parsed_expression.evalf()
    except:
        return "invalid input"
    return result

while True:
    expression = input("Enter calculation: ")
    if expression.strip().lower() == 'exit':
        print("Exiting program...")
        break
    result = calculate(expression)
    print(result)
