# 5) Реализуйте алгоритм перемешивания списка.

import random

def mesh(List):
    last_index = len(List) - 1
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        List[last_index], List[rand_index] = List[rand_index], List[last_index]
        last_index -= 1
    return List

num = int(input('Введите положительное целое число N: '))
numList = []
while num <= 0:
    print('Введено отрицательное число!!!')
    break
else:
    for i in range(num):
        numList.append(i+1)
    print(f'Изначальный  список: {numList}')
    mesh(numList)
    print(f'Перемешанный список: {numList}')
