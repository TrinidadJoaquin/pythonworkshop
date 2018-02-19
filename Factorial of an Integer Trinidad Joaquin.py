from math import*

sum=0
x=input("Give a number: ")
for i in range(1,x):
    print (i,"squared is",i*i)
    sum = sum + (i*i)
print "sum of first ", x-1 ," squares is ", sum

raw_input("Press ENTER to exit")
