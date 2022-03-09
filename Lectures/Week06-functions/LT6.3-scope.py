# More messing with functions
# variable scope

from re import X


x = 7                            # this variable applies throughout (it's a global variable)

def toPower(number, power = 3):
    x = 3                 # this variable only applies to the paragraph (within the defined function)
    print("in function", x)    
    return number ** power

answer = toPower(num)
print ("cube of", num, "is", answer)

toPower(4)
print("outside the function x is", x)    # this x will be 7 (the global variable)

# try and encapsulate all the data you need in a function to either come in
# through the arguments and out through the return statement
# all the variables should just be inside the function
# do not use global vairables
# if you really need to use one then usea class one - to be covered later

