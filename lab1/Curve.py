from Point import Point
from Interval import Interval
from Line import Line


class Curve:
    """
    Класс кривой
    """

    def __init__(self, qp, width, height, parameter, step, travel, turn):
        # Место рисования
        self.__qp = qp

# Параметры для перемещения
        # for X
        self.__phi = turn.get_turn()
        self.__b = width / 2 - travel.calculate_travel_x()
        self.__m = 5 * width / 270
        # for Y
        self.__k = -5 * height / 280
        self.__a = height / 2 - travel.calculate_travel_y()

# изменяющиеся параметры кривой
        self.__parameter = parameter
        self.__center = 0
        self.__interval = Interval(self.__center, self.__parameter, step)
        self.__step = step
        self.__width = width
        self.__height = height

# Рисование кривой
    def draw(self):
        start_T = self.__interval.getStart()
        x = self.__calculateValueX(start_T)
        y = self.__calculateValueY(start_T)
        point_start = Point(x, y)
        for t in self.__interval:
            x = self.__calculateValueX(t)
            y = self.__calculateValueY(t)
            point_end = Point(x, y)
            line = Line(point_start, point_end)
            line.to_turn(self.__phi)
            line.to_scale(self.__m, self.__k)
            line.move(self.__b, self.__a)
            line.draw(self.__qp)
            point_start = Point(x, y)

# Вычисление координаты х
    def __calculateValueX(self, t):
        return t

# Вычисление координаты у
    def __calculateValueY(self, t):

        y = (self.__parameter**(2 / 3) - (t**2) ** (1 / 3))**(3 / 2)
        return y
