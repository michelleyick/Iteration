#Michelle Yick
#10-11-2014
#Guess the number game.

import random
number = random.randint(1,100)

count=0

valid = False

while not valid:
    guess=int(input("Please enter a guess between 1 to 100:"))
    if guess == number:
        count = count+1
        valid = True
        print("You guessed the number! It was {0}, it took you {1} tries.".format(number,count))
    elif 0 <= guess < number:
        count = count+1
        print("Your guess is too low, please try again.")
    elif number <= guess < 100:
        count = count+1
        print("Your guess is too high, please try again.")
    else:
        print("You entered a number out of range, please enter a nubmer inbetween 1-100.")
