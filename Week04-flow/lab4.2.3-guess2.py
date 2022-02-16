# This program modifies guess1.py to tell the user if the guess was too high or low each time they guess
# Author: Éilis Sutton

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:           # I know it can't be equal or too low, so it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess)