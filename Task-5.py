'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
[Негафибоначчи, см. Википедию]
'''

def FibonacciNumbers(x):
    FibonacciList = []
    a, b = 1, 1

    for i in range(x - 1):       # положительные числа
        FibonacciList.append(a)
        a, b = b, a + b
    a, b = 0, 1

    for i in range(x):           # отрицательные числа
        FibonacciList.insert(0, a)
        a, b = b, a - b

    return FibonacciList

n = int(input('Введите число: ')) + 1
FibonacciList = FibonacciNumbers(n)
print(FibonacciList)