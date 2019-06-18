__author__ = 'Крымов Иван'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        def side_len(point_1, point_2):
            return math.sqrt((point_1[0] - point_2[0]) ** 2
                             + (point_1[1] - point_2[1]) ** 2)

        self.ab = side_len(a, b)
        self.bc = side_len(b, c)
        self.ca = side_len(c, a)

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def square(self):
        return math.sqrt(
            (self.perimeter() / 2) * ((self.perimeter() / 2) - self.ab) * (
                    (self.perimeter() / 2) - self.bc) * ((self.perimeter() / 2) - self.ca))

    def high_a(self):
        return 2 * self.square() / self.bc

    def high_b(self):
        return 2 * self.square() / self.ca

    def high_c(self):
        return 2 * self.square() / self.ab


print()
triangle_1 = Triangle([10, 10], [-20, -20], [30, 0])
print(f'Площадь треугольника: {triangle_1.square()}')
print(f'Высота треугольника из точки a: {triangle_1.high_a()}')
print(f'Высота треугольника из точки b: {triangle_1.high_b()}')
print(f'Высота треугольника из точки c: {triangle_1.high_c()}')
print(f'Периметр треугольника: {triangle_1.perimeter()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        def side_len(point_1, point_2):
            return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

        self.ab = side_len(a, b)
        self.bc = side_len(b, c)
        self.cd = side_len(c, d)
        self.da = side_len(d, a)
        self.ac = side_len(c, a)

    def is_equilateral(self):
        if self.ab == self.cd or self.bc == self.da:
            return True
        return False

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def square(self):
        self.perimeter_1 = self.ab + self.bc + self.ac
        self.perimeter_2 = self.cd + self.da + self.ac
        return math.sqrt( self.perimeter_1 * (self.perimeter_1 - self.ab) * (self.perimeter_1 - self.bc) * (self.perimeter_1 - self.ac)) + math.sqrt( self.perimeter_2 * (self.perimeter_2 - self.cd) * (self.perimeter_2 - self.da) * (self.perimeter_2 - self.ac))
print()
trapeze_1 = Trapeze([10, 10], [-20, -20], [30, 0], [-30,0])

print(f'Периметр трапеции: {trapeze_1.perimeter()}')
print(f'Проверка равнобедренная ли трапеция? {trapeze_1.is_equilateral()}')
print(f'Площадь трапеции: {trapeze_1.square()}')