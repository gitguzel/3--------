# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
#Пример:* для k = 8 список будет выглядеть так: 
#[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

print("Введите число:")
k = int(input("Введите число:"))
def fibonacciPos(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
dataPos = list(fibonacciPos(k))
print(f"Для числа {k} список чисел Фибоначи:{dataPos}")
def fibonacciNeg(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b
dataNeg = list(fibonacciNeg(k))
print(f"Для числа {k} список чисел Негфибоначи: {dataNeg}")
dataRes = dataNeg + [0] + dataPos
print(f"Для числа {k} список чисел Фибоначчи,в том числе для отрицательных индексов: {dataRes}")
