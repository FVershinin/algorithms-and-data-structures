def calculator():
    operation = ""
    while operation != "0":
        operation = input("Please select operation (+, -, *, / and 0 for exit):")
        if operation == "+":
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
            print(f'{a} + {b} = {a + b}')
        elif operation == "-":
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
            print(f'{a} - {b} = {a - b}')
        elif operation == "*":
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
            print(f'{a} * {b} = {a * b}')
        elif operation == "/":
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
            print(f'{a} / {b} = {a / b}')
        else:
            print("Incorrect operation")

