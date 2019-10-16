from Point import Point
from Line import Line
import numpy as np


class CordinateAxes():
    def __init__(self, width, height, travel, scale):
        self.__width = width
        self.__height = height
        self.__travel = travel
        self.scale = scale
        self.__axes = []
        self.__create()

    def __create_axes_ox(self):
        y = self.__height / 2 - self.__travel.calculate_travel_y()
        start = Point(0, y)
        end = Point(self.__width, y)
        start_arrow_line_up = Point(self.__width - 10, y + 5)
        start_arrow_line_down = Point(self.__width - 10, y - 5)
        ticks1 = [Line(Point(i, y + 3), Point(i, y - 3))
                  for i in np.arange(self.__width / 2, 0, -self.scale)]
        ticks2 = [Line(Point(i, y + 3), Point(i, y - 3))
                  for i in np.arange(self.__width / 2, self.__width, self.scale)]
        return ticks1 + ticks2 + [Line(start, end), Line(start_arrow_line_up, end), Line(start_arrow_line_down, end)]

    def __create_axes_oy(self):
        x = self.__width / 2 - self.__travel.calculate_travel_x()
        start = Point(x, 0)
        end = Point(x, self.__height)
        start_arrow_line_up = Point(x - 5, 10)
        start_arrow_line_down = Point(x + 5, 10)
        ticks1 = [Line(Point(x + 3, i), Point(x - 3, i))
                  for i in np.arange(self.__height / 2, 10, -self.scale)]
        ticks2 = [Line(Point(x + 3, i), Point(x - 3, i))
                  for i in np.arange(self.__height / 2, self.__height, self.scale)]
        return ticks1 + ticks2 + [Line(start, end), Line(start_arrow_line_up, start), Line(start_arrow_line_down, start)]

    def __create(self):
        self.__axes += self.__create_axes_ox()
        self.__axes += self.__create_axes_oy()

    def draw(self, qp):
        for line in self.__axes:
            line.draw(qp)
