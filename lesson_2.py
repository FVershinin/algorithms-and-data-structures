# 1
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


# 2
def count_number_type():
    text = input("please enter number:")
    even_numbers = 0
    odd_numbers = 0
    for symbol in text:
        number = int(symbol)
        if number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    print(f'odd numbers: {odd_numbers}, even numbers: {even_numbers}')


# 3
def reverse():
    text = input("Enter text::")

    print(text[::-1])


# 4
def sum():
    for i in range(0, int(input("Enter count"))):
        print(1 / pow(2, i) * (1 if i % 2 == 0 else -1))

# 6
import random


def _random():
    secret_value = random.randint(0, 100)
    for i in range(10):
        value = int(input("Please enter number"))
        if secret_value == value:
            print('You guessed the number!')
            break
        else:
            print(f'The secret number is {"greater" if secret_value > value else "less"}')
    print(f'Secret number is ${secret_value}')

# 8
def calculate_numbers_in_sequence():
    numbers = input("Enter numbers")
    assert numbers.isdigit()
    number = input("Enter number")
    assert number.isdigit()
    results = 0
    for symbol in numbers:
        if symbol == number:
            results += 1;
    print(results)
