#Michelle Yick
#19-10-2014
#Iteration class exercises. Revision Q2.

message = input("Please enter the message that you would like to have repeated.") 
repeats = int(input("How many times would you like your message to be repeated?"))
if repeats > 0:
    for counter in range(repeats): 
        print(message)
elif repeats < 0:
    print("You have entered an invalid value.")
    

