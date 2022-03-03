# this program reads in 2 numbers then multiplies them

# try/except below catches a user input error. i.e inputting a string type instead of integer

num1 = False
while (num1 == False):
    try:
        num1 = int(input("Enter a number: "))
    except ValueError:
        print("No strings please, ", end="")

num2 = False
while (num2 == False):
    try:
        num2 = int(input("Enter another number: "))
    except ValueError:
        print("No strings please, ", end="")


answer = num1 * num2

# print("{} multiplied by {} is {}".format(num1, num2, answer))
# can use a different format than the one above

print(f"{num1} multiplied by {num2} is {answer}")



