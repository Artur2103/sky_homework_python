import math


def square(side):
    return math.ceil(side) ** 2


side = float(input("Введите значение стороны квадрата: "))
print(f"Площадь квадрата равна:  {square(side)}")
