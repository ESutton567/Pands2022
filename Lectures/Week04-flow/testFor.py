# Messing with 'For loops'
# Author: Éilis Sutton

# for elm in list:
    # do something

# for number in  range(1,10):
    # do something

# 1
boats = ['Sigma', 'Beneteau', 'Swam'] 

for boat in boats:
        print ("I'd prefer to be out on a " + boat)
print ("out on the water")             # Not in the for loop so will only come out at the end
# Indent to include in for loop

# 2
boats = ['Sigma', 'Beneteau', '99']                      # We have a number in the list...

for boat in boats:
        print ("I'd prefer to be out on a " + str(boat)) # ...so we need to cast it to a string

# 3
for number in range(1,10):              # This will count from 1 to 9 (one less than second value in range)
    print("hello ", number)           
