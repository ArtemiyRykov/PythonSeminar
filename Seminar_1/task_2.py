# Написать программу которая принимает пять чисел и находит максимальное из них

from random import random


import random

lst = []
for i in range(5):
    lst.append(random.randint(1,100))
print(lst) 
max = lst[0]
for i in lst:
    if max < i:
        max = i
print(max)           