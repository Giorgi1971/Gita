import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return str(f'Point: ({self.__x}, {self.__y}')

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, a, b):
        return math.hypot(abs(self.__x - a), abs(self.__y - b))

    def distance_from_point(self, point):
        return math.hypot(abs(self.__x - point.getx()), abs(self.__y - point.gety()))


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
