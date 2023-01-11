import re

def calculate(expression):
    match = re.search("(\d+\.?\d*)\s*([+\-*/])\s*(\d+\.?\d*)", expression)
    if match:
        num1, operator, num2 = match.groups()
        num1, num2 = float(num1), float(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "invalid input"
            return num1 / num2
    else:
        return "invalid input"

while True:
    expression = input("Enter calculation: ")
    if expression.strip().lower() == 'exit':
        print("Exiting program...")
        break
    result = calculate(expression)
    print(result)
