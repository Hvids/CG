from get_float_range import get_float_range


class Interval:
    """
    Интервал, который пробегает t
    """

    def __init__(self, center, end, step):
        self.__center = center
        self.__radius = end
        self.__step = step
        self.__point_list = self.__calculatePointList()
        self.__limit = len(self.__point_list)
        self.__cursor = -1

    def getInterval(self):
        return self.__point_list

    def getStart(self):
        return self.__point_list[0]

# Вычисляем мнрожество точек
    def __calculatePointList(self):
        list_plus = []
        list_minus = []
        for t in self.__getFloatRangePlus():
            list_plus.append(t)
        if list_plus[-1] < self.__radius:
            list_plus.append(self.__radius)
        for t in self.__getFloatRangeMinus():
            list_minus.append(t)
        return list_minus + list_plus

# Получить массив который больше или равен центра
    def __getFloatRangePlus(self):
        return get_float_range(self.__center, self.__radius + self.__center, self.__step)

# Получить массив который меньше центра
    def __getFloatRangeMinus(self):
        return get_float_range(self.__center - self.__radius, self.__center, self.__step)

# Переопределил операторы
    def __iter__(self):
        return iter(self.__point_list)

    def __next__(self):
        if self.__cursor < self.__limit - 1:
            self.__cursor += 1
            return self.__point_list[self.__cursor]
        else:
            return StopIteration

    def __str__(self):
        return '[ ' + str(self.__interval[0]) + ';' + str(self.__interval[-1]) + ' ]'
