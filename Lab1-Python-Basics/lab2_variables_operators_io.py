"""
Lab Exercise 2: Programs using variables, operators, and input/output.
Demonstrates variable declaration, arithmetic/relational/logical operators,
and taking input from the user.
"""

def main():
    # Variables
    a = 10
    b = 3
    name = "Hani"

    # Arithmetic operators
    print("---- Arithmetic Operators ----")
    print(f"a = {a}, b = {b}")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Floor Division: {a // b}")
    print(f"Modulus: {a % b}")
    print(f"Exponent: {a ** b}")

    # Relational operators
    print("\n---- Relational Operators ----")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a == b: {a == b}")

    # Logical operators
    print("\n---- Logical Operators ----")
    print(f"(a > 5) and (b < 5): {(a > 5) and (b < 5)}")
    print(f"(a > 5) or (b > 5): {(a > 5) or (b > 5)}")
    print(f"not (a > 5): {not (a > 5)}")

    # Input / Output
    print("\n---- Input / Output ----")
    user_num1 = float(input("Enter first number: "))
    user_num2 = float(input("Enter second number: "))
    print(f"Sum of {user_num1} and {user_num2} is {user_num1 + user_num2}")


if __name__ == "__main__":
    main()
