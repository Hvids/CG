from Point import Point


class TravelScreen:
    def __init__(self):
        self.point_start = Point(0, 0)
        self.point_end = Point(0, 0)
        self.__travel_x = 0
        self.__travel_y = 0

    def update_travel(self):
        self.__travel_x += (self.point_end.x - self.point_start.x)
        self.__travel_y += (self.point_end.y - self.point_start.y)

    def calculate_travel_x(self):
        return self.__travel_x

    def calculate_travel_y(self):
        return self.__travel_y

    def __str__(self):
        return f'{self.__travel_x}, {self.__travel_y}'
