# More messing with functions
# flexible arguments

print ("hi", 55, 343, [], {}, sep=":")

# flexible number of arguments

def flex1(*args):
    print (type(args))
    for x in args:
        print(x)
        # need to call this function next for anything to print out

flex1(1, 2, 3)

# keyword items

def flex2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print (f"{key} is {value}") # this is a handy way of formatting strings

flex2(age = 23, title ="hi")  # this will pass in 2 arguments into this function (flex 2) 
                              # and it will take it as a dictionary object 
    