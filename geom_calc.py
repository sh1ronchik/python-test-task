import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))