# This program prompts the user to guess a number and keep guessing until they get it right
# Author: Éilis Sutton

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
        print("Wrong")
        guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", numberToGuess)

