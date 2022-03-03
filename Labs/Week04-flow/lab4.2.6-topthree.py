# This program generates 10 random numbers (0-100)
# It then prints them out followed by printing the top three

# Use a list to store and manipute the numbers

import random
# Program the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (0,10):         #???
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}".format(howMany,numbers))

# Keep the original list
# Sort and split the list idea from: 
# https://stackoverflow.com/questions/32296887/how-to-find-the-1st-2nd-3rd-highest-values-in-a-list-in-python
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))
