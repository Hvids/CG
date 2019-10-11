from math import cos, sin, pi


class Transform:
    """
        Базовый класс для перобразований
    """

    def __mul__(self, point):
        point = [point.x, point.y, point.z, 1]
        res = []
        for row in self.matrix:
            sum = 0
            for i in range(len(row)):
                sum += (row[i] * point[i])
            res.append(sum)
        return (res[0], res[1], res[2])


class TurnOX(Transform):
    """
        Поворот вокруг оси ОХ
    """

    def __init__(self, phi=0):
        self.matrix = [
            [1, 0, 0, 0],
            [0, cos(phi), -sin(phi), 0],
            [0, sin(phi), cos(phi), 0],
            [0, 0, 0, 1]
        ]


class TurnOY(Transform):
    """
        Поворот вокруг оси ОУ
    """

    def __init__(self, phi=0):
        self.matrix = [
            [cos(phi), 0, sin(phi), 0],
            [0, 1, 0, 0],
            [-sin(phi), 0, cos(phi), 0],
            [0, 0, 0, 1]
        ]


class TurnOZ(Transform):
    """
        Поворот вокруг оси ОZ
    """

    def __init__(self, phi=0):
        self.matrix = [
            [cos(phi), -sin(phi), 0, 0],
            [sin(phi), cos(phi), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]


class Moving(Transform):
    """
        Перемещение(Центрирование)
    """

    def __init__(self, d_x=0, d_y=0, d_z=0):
        self.matrix = [
            [1, 0, 0, d_x],
            [0, 1, 0, d_y],
            [0, 0, 1, d_z],
            [0, 0, 0, 1]
        ]


class Scale(Transform):
    """
        Маштабировние
    """

    def __init__(self, k_x=0, k_y=0, k_z=0):
        self.matrix = [
            [k_x, 0, 0, 0],
            [0, k_y, 0, 0],
            [0, 0, k_z, 0],
            [0, 0, 0, 1]
        ]


class OrthographicProjectionX(Transform):
    """
        Ортографическое проецирование на плоскость ZY (X = 0)
    """

    def __init__(self):
        self.matrix = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]


class OrthographicProjectionY(Transform):
    """
        Ортографическое проецирование на плоскость ZX (Y = 0)
    """

    def __init__(self):
        self.matrix = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]


class OrthographicProjectionZ(Transform):
    """
        Ортографическое проецирование на плоскость XY (Z = 0)
    """

    def __init__(self):
        self.matrix = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ]


class IsometricTransform(Transform):
    """
        Изметрическая проекция
    """

    def __init__(self, phi=(-pi / 4), tetta=(pi / 5)):
        self.matrix = [
            [cos(tetta), sin(tetta) * cos(phi), 0, 0],
            [0, cos(phi), 0, 0],
            [sin(tetta), -cos(tetta) * sin(phi), 0, 0],
            [0, 0, 0, 1]
        ]
