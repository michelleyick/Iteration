#Michelle Yick
#12-11-2014
#Iteration spotcheck Q2.

total = 0
number = int(input("Please enter an integer:"))

for count in range(1,13):
    total = count*number
    print("{0:>3} *{1:>3} = {2:>3}".format(count,number,total))
