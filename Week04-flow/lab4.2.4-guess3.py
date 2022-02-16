# This program generates a random number between 1-100 to guess
# Author: Éilis Sutton
# Ref 1: https://www.codegrepper.com/code-examples/python/return+a+random+number+between+0+and+100+python
# Ref 2: https://www.programiz.com/python-programming/examples/random-number

# Generate a random number
import random                   
numberToGuess = random.randint(1,100)

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:           # I know it can't be equal or too low, so it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess)

