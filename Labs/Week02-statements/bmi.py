# This program calculates BMI (kg/m2)
# Author: Éilis Sutton

# We must convert the string that input returns to an int
# Height must be converted to cm as decimal point numbers (kg value) cannot be computed to base 10
weight = int(input("Please enter your weight (kg):"))
height = int(input("Please enter your height (cm):"))
newNumber = weight/((height/100)**2)
print('The BMI is kg/m2: {}' .format (newNumber))

