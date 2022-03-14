# This program reads in a number from a file that already exists (count.txt)
# Author: Éilis Sutton

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read() )
        return number

# test it
num = readNumber()
print (num)