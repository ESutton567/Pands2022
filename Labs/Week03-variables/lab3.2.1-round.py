# This program rounds a number
# NB Be careful of round as it rounds to the nearest EVEN number
# E.g. 4.5 rounds to 4; 5.5 rounds to 6
# Do not use if accuracy is essential
# Author: Éilis Sutton

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))
