# This program prints out a random fruit
# Author: Éilis Sutton

import random


import random

# A list is square brackets []
fruits = ['Apple', 'Mango', 'Passionfruit', 'Kiwi', 'Pineapple']

# We want a random number between 0 and length-1

# The len() function returns the number of items in an object. 
# When the object is a string, the len() function returns the number of characters in the string.
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))


