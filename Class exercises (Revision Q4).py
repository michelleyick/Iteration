#Michelle Yick
#28-10-2014
#Iteration class exercises. Revision Q4.

#Ask the user to input a number between 10-20. Display a message asking the user to re-enter a numbe. Program terminates when the number entered is between 10 and 20.

answer = False
while not answer:
    number = int(input("Enter a number in the range 10 to 20:"))
    
    if 10 <= number <= 20:
        answer = True
        print("You have entered a number within the range.")

