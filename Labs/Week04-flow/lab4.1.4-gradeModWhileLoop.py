# This program modifies (?)4.1.2 to use a 'while loop' ..
# ..to keep prompting user for a number until the user enters -1
# Ref: AB lecture 4.2; Lab 4.2 loops.pdf
    
# 4.1.2 This program reads in a students percentage mark and prints out the corresponding grade
# 4.1.2 The program should check that the percentage is valid
# Author: Éilis Sutton


number = int(input("Please enter a number: "))       

while number != -1:  
    number = int(input("Please enter another number: ")) 

print ("Correct")

# See lab4.2.2-guess1.py for nicer output


