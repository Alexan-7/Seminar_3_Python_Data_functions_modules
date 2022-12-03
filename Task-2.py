'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

from random import randrange
quantity = int(input('Задайте количество элементов списка: '))
list1 = [randrange(50) for i in range(quantity)]
print(f'Список случайных чисел: {list1}')

# или list1 = input('Введите элементы через пробел').split() и тогда print(int(list1))

# нечет. quantity - // + 1, четн. quantity - // + 0
i = 0
for i in range(quantity // 2 + len(list1) % 2):
     print(list1[i] * list1[quantity - i - 1], end = ' ')
     i += 1