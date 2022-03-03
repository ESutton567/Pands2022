# This program modifiies 4.1.2 to deal with the automatic rounding of 69.5 to 70 
# This would erroneously print 'Distinction

# 4.1.2: This program reads in a students percentage mark and prints out the corresponding grade
# 4.1.2: The program should check that the percentage is valid

# Author: Éilis Sutton

percentage = float(input("Enter the percentage: "))       # Print percentage

# Be careful with 'Ands' or 'Ors'
if percentage < 0 or percentage > 100: 
    print ("please enter a number between 0 and 100")
elif percentage < 39.4:                   # Instruct program to only include <39.5 or <=39.4 
    print ("Fail")                        # This covers the rounding of 39.5 up to 40 in practice
elif percentage <= 49.4:                  
    print ("Pass")
elif percentage < 50.4:                   
    print ("Merit 1")
elif percentage < 60.4:                   
    print ("Merit 2")
else:                                   # The only option left is between 70 and 100
    print ("Distinction")