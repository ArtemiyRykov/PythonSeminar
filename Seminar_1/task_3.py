# Напишите программу котороя будет на вход принимать число N и выводит число от -N до N

# N = int(input('Введите число - '))
# for i in range (-N, N+1):
#     print(i)

number = int(input('Введите число - '))
if number < 0:
    number = -number
list_of_number = []
for num in range(-number, number + 1):
    list_of_number.append(num)
print(list_of_number)    