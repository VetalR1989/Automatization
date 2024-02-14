# Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата. Если переданный аргумент был не целым, округлите результат вверх.

import math

def square(side):
    result = side ** 2
    print(result)
    if not isinstance(side, int):
        result = math.ceil(result)
    return result
side = input("Введите длину стороны квадрата: ")
side = float(side)
square(side)