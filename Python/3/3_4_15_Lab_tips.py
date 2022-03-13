import math
from itertools import combinations

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__p = [vertice1, vertice2, vertice3]

        def __str__(self):
            return str()

    def perimeter(self):
        per = 0
        for a, b in list(combinations(self.__p, 2)):
            per += math.hypot(a.x - b.x, a.y - b.y)
        return per


triangle = Triangle(Point(0, 0), Point(1, 1), Point(0, 1))
print(triangle.perimeter())
