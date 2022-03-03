# Why does this expression cause an error? How can you fix it?

# message = 'I have eaten ' + 99 + ' buttitos.'
# print (message)

""" 
Solution:
# Reference: https://automatetheboringstuff.com/appendixc/
The expression causes an error because 99 is an integer, and only strings can be concatenated to 
other strings with the + operator. The correct way is: 
"""

message = 'I have eaten ' + str(99) + ' burittos.'
print (message)