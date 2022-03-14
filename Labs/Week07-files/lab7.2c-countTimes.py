# This program counts how many times the program has been run
# Author: Éilis Sutton

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read() )
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
    # write takes a string so we need to convert
        f.write(str(number))

# main
num = readNumber()
num += 1         # this adds the currrent value to itself
print ("we have run this program {} times".format(num))