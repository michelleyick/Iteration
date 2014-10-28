#Michelle Yick
#28/10/2014
#Iteration class exercises. Revision Q5.

total = 0
numberSeries = 1
amount = int(input("Amount of numbers you want to average"))

while numberSeries != -1:
    if numberSeries > 0:
        numberSeries = int(input("Enter the series of numbers you wish to average. Seperate each number with a space."))
        total = numberSeries + total

average = total/amount
print("The average of your number series is {0}".format(average))
  
        
        

