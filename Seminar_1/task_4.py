# Напишите программу котороя будет на вход принимать дробь
# и показывать первую цифру дробной части

number = float(input('Введите дробное число - '))
if number - int(number) == 0:
    print('нет')
else:
    answer = number * 10 % 10
    # answer = number * 10
    # print(answer)
    # answer = answer % 10
    # print(answer)
    print(int(answer))   