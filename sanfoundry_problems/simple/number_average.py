""" A program to check average of numbers
"""

# Read total numbers count from the user

n = int(input("Enter the count of numbers of to calculate Average : "))
assert n > 0
number_list = []
for i in range(n):
    element = int(input(f"Enter the {i + 1} number in the list: "))
    number_list.append(element)

num_avg = sum(number_list) / n
print("the average is :", round(num_avg, 3))
