"""
Mini Project: Unit converter or bill generator.
This file implements BOTH so you can pick whichever your lab requires
(or demo both).
"""


def unit_converter():
    print("---- Unit Converter ----")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    choice = input("Choose conversion (1/2/3): ")

    if choice == "1":
        km = float(input("Enter distance in km: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == "3":
        kg = float(input("Enter weight in kg: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} lbs")
    else:
        print("Invalid choice.")


def bill_generator():
    print("\n---- Bill Generator ----")
    items = []
    n = int(input("Enter number of items: "))

    for i in range(n):
        name = input(f"Enter name of item {i + 1}: ")
        price = float(input(f"Enter price of {name}: "))
        qty = int(input(f"Enter quantity of {name}: "))
        items.append((name, price, qty))

    print("\n----------- BILL -----------")
    print(f"{'Item':<15}{'Price':<10}{'Qty':<5}{'Total':<10}")
    grand_total = 0
    for name, price, qty in items:
        total = price * qty
        grand_total += total
        print(f"{name:<15}{price:<10.2f}{qty:<5}{total:<10.2f}")

    tax = grand_total * 0.05  # 5% tax
    final_total = grand_total + tax
    print("-----------------------------")
    print(f"Subtotal: {grand_total:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Grand Total: {final_total:.2f}")
    print("-----------------------------")


if __name__ == "__main__":
    print("1. Unit Converter")
    print("2. Bill Generator")
    option = input("Choose a program to run (1/2): ")

    if option == "1":
        unit_converter()
    elif option == "2":
        bill_generator()
    else:
        print("Invalid option.")
