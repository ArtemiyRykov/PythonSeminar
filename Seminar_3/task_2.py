# 2. Напишите программу, которая определит позицию второго
#  вхождения строки в списке либо сообщит, что её нет.
#['a', 'a','b'] -> 'a' по индексу 1

n = 7
    
mylist = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']

def find_number(n, lst):
    return str(n) in lst

print(find_number(n, mylist))