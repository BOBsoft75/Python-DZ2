# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

num = (input('Введите вещественное число: '))
while num.isdigit() == False:
    print('Введено не число!!!')
    break
listNum = list(num)
sum = 0
for i in range(len(listNum)):
    if listNum[i] == '-' or listNum[i] == '.':
        continue
    if listNum[i] != '.':
        sum += int(listNum[i])
print(num, ' -> ', sum)
