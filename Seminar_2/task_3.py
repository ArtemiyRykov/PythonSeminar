# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

string1 = input('Напиши что нибудь: ')
string2 = input('Напиши что нибудь ещё разок: ')
if len(string1) < len(string2):
    string1, string2 = string2, string1
count = 0
for i in range(0, len(string1)-len(string2)+1):
    if string2.lower() == string1[i:i+len(string2)].lower():
        count += 1
    print(string1[i:i+len(string2)])
print(count)
