import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, side_1x, side_1y, side_2x, side_2y, side_3x, side_3y):
        self.side_1x = side_1x
        self.side_1y = side_1y
        self.side_2x = side_2x
        self.side_2y = side_2y
        self.side_3x = side_3x
        self.side_3y = side_3y
        # сразу рассчитаем стороны
        self.side_1 = math.sqrt((self.side_1x-self.side_2x)*(self.side_1x-self.side_2x)+(self.side_1y-self.side_2y)*(self.side_1y-self.side_2y))
        self.side_2 = math.sqrt((self.side_2x-self.side_3x)*(self.side_2x-self.side_3x)+(self.side_2y-self.side_3y)*(self.side_2y-self.side_3y))
        self.side_3 = math.sqrt((self.side_3x-self.side_1x)*(self.side_3x-self.side_1x)+(self.side_3y-self.side_1y)*(self.side_3y-self.side_1y))
        # и полупериметр
        self.half_meter = (self.side_1 + self.side_2 + self.side_3) / 2
    def area(self):  # площадь
        print((math.sqrt(self.half_meter * (self.half_meter - self.side_1) * (self.half_meter - self.side_2) * (self.half_meter - self.side_3))))

    def height(self):
        print((2 * math.sqrt(self.half_meter * (self.half_meter - self.side_1) * (self.half_meter - self.side_2) * (self.half_meter - self.side_3))) / self.side_1)

    def perimeter(self):
        print(self.side_1 + self.side_2 + self.side_3)


triangle = Triangle(2, -5, -6, 1, 6, -2)
triangle.area()
triangle.height()
triangle.perimeter()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, side_a_x, side_a_y, side_b_x, side_b_y, side_c_x, side_c_y, side_d_x, side_d_y):
        self.side_a_x = side_a_x
        self.side_a_y = side_a_y
        self.side_b_x = side_b_x
        self.side_b_y = side_b_y
        self.side_c_x = side_c_x
        self.side_c_y = side_c_y
        self.side_d_x = side_d_x
        self.side_d_y = side_d_y
        # найдем стороны
        self.side_a = math.sqrt((self.side_a_x-self.side_b_x)*(self.side_a_x-self.side_b_x)+(self.side_a_y-self.side_b_y)*(self.side_a_y-self.side_b_y))
        self.side_b = math.sqrt((self.side_b_x-self.side_c_x)*(self.side_b_x-self.side_c_x)+(self.side_b_y-self.side_c_y)*(self.side_b_y-self.side_c_y))
        self.side_c = math.sqrt((self.side_c_x-self.side_d_x)*(self.side_c_x-self.side_d_x)+(self.side_c_y-self.side_d_y)*(self.side_c_y-self.side_d_y))
        self.side_d = math.sqrt((self.side_d_x-self.side_a_x)*(self.side_d_x-self.side_a_x)+(self.side_d_y-self.side_a_y)*(self.side_d_y-self.side_a_y))

    def check(self):
        if self.side_a == self.side_c:
            print('Трапеция равнобокая')
        else:
            print('Трапеция не равнобокая')

    def lenght(self):  # раз уж длину я все равно нашел раньше...
        print(self.side_a, self.side_b, self.side_c, self.side_d)

    def perimeter(self):
        print(self.side_a + self.side_b + self.side_c + self.side_d)

    def side(self):
        print(((self.side_a + self.side_b) / 2) * math.sqrt(((self.side_c * self.side_c)-((self.side_b - self.side_a) * (self.side_b - self.side_a)) + (self.side_c * self.side_c) + (self.side_d * self.side_d)) / 2 (self.side_b - self.side_a)))

