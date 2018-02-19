import sys

from math import *

print ("Nintendo Wiis are 1000 php")
money = input("How rich are you? ")
price = 1000

if (money < price):
    diff = price - money
    print ("You don't have enough")
    print "You need ", diff ," more."
if (money >= price):
    num = money/price
    print ("You can buy! Yehey!")
    print "You can buy ", num ," Nintendo Wii/s"
    end
raw_input('Press ENTER to exit')
