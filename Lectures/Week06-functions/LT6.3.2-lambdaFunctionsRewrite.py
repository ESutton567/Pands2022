# More messing with functions
# Annonymous functions

# def doubler (num):
#    return num * 2

# def tripler (num):
#    return num * 3

# rewrite the fuctions above below as lambda (which means what follows is a function)

isMax = True
if isMax: 
    fun = lambda num : num * 2     # Annonymous function (it has no name)
else:
    fun = lambda num : num * 3          

var = fun(10)           # fun here depends on which one varaible preceeds it
print (var)

# sorted
list = [45, 89, 5, 68]
print (list)
newList = sorted (list)
print (newList)

# sort dictionary
# need to pass in a function in sorted to allow it to sort as it can't to < or > in a dict
data = [{'first': 'Mary', 'last': 'Smith', 'YOB': 1983}, 
        {'first': 'John', 'last': 'Turing', 'YOB': 1998}, 
        {'first': 'Amy', 'last': 'Bridge', 'YOB': 1952}]

newData = sorted (data, key = lambda item: item['last'])
for item in newData:
    print (item)


