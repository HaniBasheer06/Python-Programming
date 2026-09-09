"""
Lab Exercise 3: Simple calculator and area calculation programs.
"""

import math


def simple_calculator():
    print("---- Simple Calculator ----")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {num1} {op} {num2} = {result}")


def area_calculations():
    print("\n---- Area Calculation ----")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = input("Choose a shape (1/2/3): ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
        print(f"Area of circle: {area:.2f}")
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area of rectangle: {area:.2f}")
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of triangle: {area:.2f}")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    simple_calculator()
    area_calculations()
