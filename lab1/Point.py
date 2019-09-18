class Point:
    """
    Класс точки
    """

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __str__(self):
        return '( ' + str(self.__x) + ', ' + str(self.__y) + ' )'
