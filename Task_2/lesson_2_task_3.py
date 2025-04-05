# Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата. Если переданный аргумент был не целым, округлите результат вверх.

import math

def square(side):
    result = side ** 2
    if not isinstance(side, int):
        result = math.ceil(result)
    return result
side = input("Введите длину стороны квадрата: ")
side = float(side)
print(square(side))