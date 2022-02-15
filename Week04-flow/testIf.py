# Program to show the format of an if statement
# Author: Éilis Sutton

if True:
    # statements
    print("condition is true")


if False:
    # statements
    print("condition is true") # this prints nothing beacuse it is looking for lines after this one and there are none


if 2 == 2:
    print("yes the world is sane")

# Can write the below code this way but see below
if 2 != 2:
    print("I hope this is not displayed!!!")  
else:
    print("2 is not equal to 2 is false")


# might be better to write the above bit of code like below
# the logic flows better

b = 3
if b == 2:
    print("yes the world is sane")
else:
    print("b is not equal to 2")


# ELIF

aNumber = 5
if (aNumber % 2) == 0: # No need for brackets. In for clarity
    print(aNumber, "is even") # Another way of printing variables
elif (aNumber % 3) == 0: # If the number is even this won't be checked
    print(aNumber, "is divisible by 3")
else: 
    print(aNumber, "is not even or divisible by 3")

print("this will always be outputted")