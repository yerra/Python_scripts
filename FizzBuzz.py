# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:51:22 2019

@author: sriha
"""

for num in range(1,10   0):
    #print(num % 3)
    if ((num % 15) == 0):
        print('FizzBuzz')
    elif ((num % 5) == 0):
        print('Buzz')
    elif ((num % 3) == 0):
        print('Fizz')
    else:
        print(num)