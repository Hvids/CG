from Point import Point
from Interval import Interval


class Curve:
    """
    Класс кривой
    """

    def __init__(self, qp, width, height, parameter, step, travel):
        # Место рисования
        self.__qp = qp

# Параметры для перемещения
        # for X
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
            self.__qp.drawLine(point_start.getX(), point_start.getY(),
                               point_end.getX(), point_end.getY())
            point_start = point_end

# Вычисление координаты х
    def __calculateValueX(self, t):

        return self.__m * t + self.__b

# Вычисление координаты у
    def __calculateValueY(self, t):
        y = self.__k * (self.__parameter**(2 / 3) - (t**2)
                        ** (1 / 3))**(3 / 2) + self.__a
        return y
