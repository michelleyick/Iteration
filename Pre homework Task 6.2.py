#Michelle Yick
#15-10-2014
#Iteration pre homework Task 6.2

password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("You now have access to the system.")
    else:
        print("Sorry the value entered the incorrect password - please try again")
