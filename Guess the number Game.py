#Michelle Yick
#10-11-2014
#Guess the number game.

count = 0

import random
number = random.randint(1,100)

guess = int (input("Enter a number as your guess"))

while guess != number:
    guess = int (input("Enter a number as your guess"))
    if guess < 1 and guess > 100 or guess == 1 or guess == 100:
        if guess < number:
            print("Your value is too low")
            count + 1
        elif guess > number:
            print("Your guess is too high")

    elif guess > 100 or guess < 1:
        print("Invalid value")

    elif guess == number:
        print("Congrats, you guessed the correct number. You took {0} times to guess the number".format(count))
        
