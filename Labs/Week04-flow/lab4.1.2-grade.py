# This program reads in a students percentage mark and prints out the corresponding grade
# The program should check that the percentage is valid
# Author: Éilis Sutton

percentage = float(input("Enter the percentage: "))       # Print percentage

# Be careful with 'Ands' or 'Ors'
if percentage < 0 or percentage > 100:  # This should throw an error. We will cover error handling later
    print ("please enter a number between 0 and 100")
elif percentage < 40:                   # We know if is greater than 0
    print ("Fail")    
elif percentage < 50:                   # Between 40 and 49
    print ("Pass")
elif percentage < 60:                   # Between 50 and 59
    print ("Merit 1")
elif percentage < 70:                   # Between 60 and 69
    print ("Merit 2")
else:                                   # The only option left is between 70 and 100
    print ("Distinction")



