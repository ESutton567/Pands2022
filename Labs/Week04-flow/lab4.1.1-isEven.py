# This program asks the user to enter in a number, and will tell the user if the number is even or odd
# Author: Éilis Sutton

number = int(input("enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))
