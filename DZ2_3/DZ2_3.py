# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

num = int(input('Введите число N: '))
numList = {}
res = 0
for i in range(1, num+1):
    numList[i] = round(((1+1/i)**i), 2)
print('Для N =', num, numList)
for i in numList:
    res += numList[i]
print('Сумма ', res)
