# Messing with 'While loops'
# Author: Éilis Sutton

# While condition:
#   statements

count = 0
while count <10:
    print(count)
    count +=1

count = 10
while count >=0:
    print(count)
    count -=1  
print ("blast off")

val = input("Enter something (q to quit):")
while val != 'q':
    print("You said: " + val)
    val = input("(q to quit):")
print ("Goodbye")

