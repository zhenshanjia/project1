import math
def sphere(value):
    radius = float(value)
    if radius <= 0:
        raise TypeError
    return 1.33 * math.pi * radius ** 3
def cube(value):
    side = float(value)
    if side <= 0:
        raise TypeError
    return side ** 3
def cone(value1,value2):
    radius, height = float(value1), float(value2)
    if radius <= 0 or height <= 0:
        raise TypeError
    return 0.33 * math.pi * radius **3
