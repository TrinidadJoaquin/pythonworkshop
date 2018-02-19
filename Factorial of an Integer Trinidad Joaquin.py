from math import*

sum=1
x=input("Give a number: ")
for i in range(1,x+1):
    print (i,"squared is",i*i)
    sum=sum*i
print "sum of first ", x ," squares is ", sum

raw_input("Press ENTER to exit")
