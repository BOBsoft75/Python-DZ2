# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

import random
num = int(input('Введите положительное целое число N: '))
numList = []
while num <= 0:
    print('Введено отрицательное число!!!')
    break
else:
    for i in range(num):
        numList.append(random.randrange(-num, num+1))
    print(numList)
    pos1 = int(input('Введите позицию(индекс) 1: '))
    pos2 = int(input('Введите позицию(индекс) 2: '))
    res = numList[pos1] * numList[pos2]
    print(f'Произведение элементов: ([{pos1}]: {numList[pos1]}, [{pos2}]: {numList[pos2]}) = {res}')
