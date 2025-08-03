def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

def run_calculator():
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))
        result = calculate(a, b, operator)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid number entered")

# Uncomment this to run as a script
if __name__ == "__main__":
    run_calculator()
