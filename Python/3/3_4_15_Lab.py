from ast import Str
import math
from turtle import st


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

        def __str__(self):
            return str()

    def perimeter(self):
        a = math.hypot(self.vertice1.x - self.vertice2.x, self.vertice1.y - self.vertice2.y) 
        b = math.hypot(self.vertice2.x - self.vertice3.x, self.vertice2.y - self.vertice3.y) 
        c = math.hypot(self.vertice1.x - self.vertice3.x, self.vertice1.y - self.vertice3.y) 
        return a+b+c


triangle = Triangle(Point(0, 0), Point(1, 1), Point(0, 1))
print(triangle.perimeter())
