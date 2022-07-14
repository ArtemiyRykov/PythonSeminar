# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
#[',hfh5', '5', 'dfgh']

lst = ['rrr', '5', '66', 'ttt7', 'fff']
    
def find_number(lst, num):
    num = str(num)
    for elem in lst:
        for i in elem:
            if i == num:
                return True
    return False
print(find_number(lst, 7))
