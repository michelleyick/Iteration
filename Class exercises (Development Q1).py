#Michelle Yick
#05-11-2014
#Iteration class exercises. Development Q1.

total = 1
n = int(input("What number would you like to work out the factorial of?"))

for nFactorial in range(1,n + 1):
    total *= nFactorial
    print(total)
