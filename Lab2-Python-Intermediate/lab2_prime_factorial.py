"""
Lab Exercise 2: Prime number and factorial programs.
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    print("---- Prime Number Check ----")
    num = int(input("Enter a number to check if it is prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    print("\n---- Factorial ----")
    fact_num = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {fact_num} is {factorial(fact_num)}")


if __name__ == "__main__":
    main()
