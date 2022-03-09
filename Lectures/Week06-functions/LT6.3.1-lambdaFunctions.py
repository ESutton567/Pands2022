# More messing with functions
# Annonymous functions


def doubler (num):
    return num * 2

def tripler (num):
    return num * 3


isMax = True
if isMax: 
    fun = doubler
else:
    fun = tripler          

var = fun(10)           # fun here depends on which one varaible preceeds it
print (var)




# fun = doubler
# fun = tripler           # this overwrites the above variable