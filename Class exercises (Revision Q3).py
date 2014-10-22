#Michelle Yick
#22-10-2014
#Iteration class exercises. Revision Q3.

#Program that asks the user the amount of numbers they want to be averaged and the actual numbers. ou then want to average them and display the average.

total = 0
amount = int(input("Enter the amount of numbers you want to average:"))

for number in range(1,amount + 1):
    number = int(input("Enter the number you want to be averaged:"))
    total = total + number

average = total/amount
print("The average of the numbers you have entered is {0}".format(average))

    
