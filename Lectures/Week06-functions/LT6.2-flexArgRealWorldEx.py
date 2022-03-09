# Real world example of whn you might use the flexible argument program

def flex2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print (f"{key} is {value}") 

# flex2(age = 23, title ="hi")  


# want to write a function to get the average of something
def ave(*args):         # get average of a list of arguments
    sumofNumbers = sum(args)
    length = len (args)
    return sumofNumbers/length

print(ave(2,3,4))
                              