"""
Lab Exercise 3: Fibonacci series using recursion.
"""


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_series(count):
    print(f"Fibonacci series up to {count} terms:")
    series = [fibonacci(i) for i in range(count)]
    print(", ".join(str(num) for num in series))


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print_fibonacci_series(n)
