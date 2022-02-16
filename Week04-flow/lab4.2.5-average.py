# This program keeps reading numbers until the user enters a 0 
# The program appends each of them into a list
# The program then prints out each of the numbers entered and the average of them

numbers = []

# First get the user to input the number. Then check if it is 0 in the while loop
number = int(input("Enter a numner (0 to quit): "))

while number != 0:
    numbers.append(number)

    # Read the next number and check if it is 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

# We want avergae to be a float
average = float(sum(numbers)) / len(numbers)     # Divided by the length of the list of numbers
print ("The average is {}".format(average))
