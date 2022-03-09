# the problem with readinnumbers.py is that there is repetitive code
# the solution would be to put it into a function

def readNum(message = "Enter a number: "):  # message will default to this text
    num = False                        # tab the code in to put it into the fx
    while (not num):                   # this is a neater way of writing it
        try:
            num = int(input(message))       # entering message instead of having the text here allows to alter the message
        except ValueError:
            print("No strings please, ", end="")
    return num

num1 = readNum()            # asks to read the code,
num2 = readNum("Enter another number: ")            # and again but alters the message

answer = num1 * num2

# print("{} multiplied by {} is {}".format(num1, num2, answer))
# can use a different format than the one above

print(f"{num1} multiplied by {num2} is {answer}")



