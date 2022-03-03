# This program reads in two numbers and outputs the integer answer and remaninder
# Author: Éilis Sutton

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y)  # // gives the int division
remainder = x%y     # % gives  the remainder

print ("{} divided by {} is {} with remainder {}".format ( x , y, answer, remainder))

