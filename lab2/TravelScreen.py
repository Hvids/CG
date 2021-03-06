from Point import Point


class TravelScreen:
    def __init__(self):
        self.point_start = Point(0, 0)
        self.point_end = Point(0, 0)
        self.__travel_x = 0
        self.__travel_y = 0

    def update_travel(self):
        self.__travel_x += (self.point_end.x - self.point_start.x) / 25
        self.__travel_y += (self.point_end.y - self.point_start.y) / 25

    @property
    def travel_x(self):
        return 5 * self.__travel_x

    @property
    def travel_y(self):
        return 5 * self.__travel_y
