#Michelle Yick
#29/10/2014
#Iteration class exercises. Revision Q5.

total = 1
numberSeries = 1
amount = int(input("Amount of numbers you want to average"))

while numberSeries != -1:
    if numberSeries > 0 or numberSeries < -1 or numberSeries == 0:
        numberSeries = int(input("Enter the number you wish to average"))
        total = numberSeries + total

average = total/amount
print("The average of your number series is {0}".format(average))
  
        
        

