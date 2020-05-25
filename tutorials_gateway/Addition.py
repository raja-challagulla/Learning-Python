""" Addition of two numbers
"""

import os

a = int(input("Enter a number : "))
b = int(input("Enter 2nd number : "))

print(a+b)
print(f"The addition of {a} and {b} is : {a + b}")

print(os.getcwd())
os.chdir("../")
print(os.getcwd())