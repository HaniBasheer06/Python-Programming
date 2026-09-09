"""
Mini Project: OTP generator or student grading automation.
This file implements BOTH so you can pick whichever your lab requires
(or demo both).
"""

import random
import string


def generate_otp(length=6, use_letters=False):
    if use_letters:
        chars = string.ascii_uppercase + string.digits
    else:
        chars = string.digits
    otp = "".join(random.choice(chars) for _ in range(length))
    return otp


def otp_generator_demo():
    print("---- OTP Generator ----")
    length = int(input("Enter OTP length (e.g. 6): "))
    otp = generate_otp(length)
    print(f"Your OTP is: {otp}")
    print("(This OTP is valid for demonstration purposes only.)")


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F (Fail)"


def student_grading_automation():
    print("\n---- Student Grading Automation ----")
    n = int(input("Enter number of students: "))
    records = []

    for i in range(n):
        name = input(f"Enter name of student {i + 1}: ")
        marks = float(input(f"Enter marks of {name} (out of 100): "))
        grade = calculate_grade(marks)
        records.append((name, marks, grade))

    print("\n----------- GRADE REPORT -----------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
    for name, marks, grade in records:
        print(f"{name:<15}{marks:<10.1f}{grade:<5}")
    print("-------------------------------------")


if __name__ == "__main__":
    print("1. OTP Generator")
    print("2. Student Grading Automation")
    option = input("Choose a program to run (1/2): ")

    if option == "1":
        otp_generator_demo()
    elif option == "2":
        student_grading_automation()
    else:
        print("Invalid option.")
