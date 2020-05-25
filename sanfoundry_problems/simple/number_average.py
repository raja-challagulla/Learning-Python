""" A program to check average of numbers
"""

# calculate the count of numbers in the program

number_list = []
while True:
    element = input("Enter the numbers to calculate Average. Once done entering the numbers enter q to stop: ")
    if element == 'q':
        break
    else:
        number_list.append(int(element))

num_avg = sum(number_list) / len(number_list)
print("the average is :", round(num_avg, 2))
