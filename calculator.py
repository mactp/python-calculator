def calc(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "unknown operator"

again = "y"
while again == "y":
    try:
        a = float(input("first number: "))
        op = input("operator: ")
        b = float(input("second number: "))
        result = calc(a, op, b)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    again = input("do you want to continue? (y/n): ")