#Michelle Yick
#12-11-2014
#Iteration spotcheck Q3.

noOfTurns = 0

import random
number = random.randint(1,100)
guessed = number

while guessed != number:
    noOfTurns = noOfTurns + 1
    userGuess = int(input("Enter your guess for the number:"))
    if userGuess == number:
       print("You guessed the correct number.")
    elif userGuessed > number:
        print("The number you have is too high")
    else:
        print("The number you guessed it too low")
   
print("You took {0} turns to guess the number. The number was {1}.".format(noOfTurns,number))
        
