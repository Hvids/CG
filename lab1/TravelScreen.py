
class TravelScreen:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.end_x = x
        self.end_y = y

    def calculate_travel_x(self):
        return -self.start_x + self.end_x

    def calculate_travel_y(self):
        return -self.start_y + self.end_y
