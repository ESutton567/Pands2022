# This program prints out a random number from within a user specificed min and max
# Author: Éilis Sutton
# Reference: https://stackoverflow.com/questions/39996814/how-to-generate-random-numbers-in-range-from-input

import random

a = int(input("Select min: "))
b = int(input("Select max: "))
number = random.randint(a, b)

print("Here is a random number within your min and max numbers -> {}".format(number))