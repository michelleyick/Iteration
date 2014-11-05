#Michelle Yick
#01-11-2014
#Iteration class exercises. Development Q1.

factor = 1
n = int(input("What number would you like to work out the factorial of?"))


if n < 0:
    print("Invalid value")
elif n == 0:
    print("The factorial of 0 is 1.")

else:
     for i in range(1,n + 1):
        factor = factor*i 
        print(factor)
        

