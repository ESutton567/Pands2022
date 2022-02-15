# This program gives the abolute value of a number
# Author: Éilis Sutton

# In the question the number format is ambiguous but looking at the output it implies a float
# So cast the input to a float

number = float(input("Enter a number: "))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number,absoluteValue))
