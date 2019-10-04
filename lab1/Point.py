from math import cos, sin


class Point:
    """
    Класс точки
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def to_turn(self, phi):
        phi = phi / 100
        x = self.x
        y = self.y
        self.x = x * cos(phi) - y * sin(phi)
        self.y = +x * sin(phi) + y * cos(phi)

    def to_scale(self, k_x, k_y):
        x = self.x
        y = self.y
        self.x = k_x * x
        self.y = k_y * y

    def move(self, h, g):
        self.move_x(h)
        self.move_y(g)

    def move_x(self, h):
        x = self.x
        self.x = x + h

    def move_y(self, g):
        y = self.y
        self.y = g + y

    def __str__(self):
        return '( ' + str(self.x) + ', ' + str(self.y) + ' )'
