from Figure import Figure
from Point import Point
from Line import Line
from Plane import Plane


class Wedge(Figure):
    def __init__(self, a, b, c, h):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.__create()

    def __create(self):
        one = Point(-self.a / 2, self.b / 2, 0)
        two = Point(self.a / 2, self.b / 2, 0)
        three = Point(self.a / 2, -self.b / 2, 0)
        four = Point(-self.a / 2, -self.b / 2, 0)
        five = Point(-self.c / 2, 0, self.h)
        six = Point(self.c / 2, 0, self.h)
        line12 = Line(one, two)
        line14 = Line(one, four)
        line15 = Line(one, five)
        line23 = Line(two, three)
        line26 = Line(two, six)
        line34 = Line(three, four)
        line36 = Line(three, six)
        line45 = Line(four, five)
        line56 = Line(five, six)
        plane1234 = Plane([line12, line14, line23, line34], one, two, three)
        plane154 = Plane([line15, line14, line45], one, five, four)
        plane236 = Plane([line23, line26, line36], two, three, six)
        plane1265 = Plane([line12, line15, line56, line26], one, two, five)
        plane5643 = Plane([line56, line36, line34, line45], five, four, three)
        self.planes.append(plane1234)
        self.planes.append(plane154)
        self.planes.append(plane236)
        self.planes.append(plane1265)
        self.planes.append(plane5643)
