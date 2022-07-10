# является ли квадрат числа

a = int(input('Введите число a = '))
b = int(input('Введите число b = '))
if a * a == b:
    print('да')
elif b * b == a:
    print('да')
else:
    print('нет')        