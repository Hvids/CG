class Turn:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.__phi = 0

    def update_turn(self):
        self.__phi += (self.end - self.start)

    @property
    def phi(self):
        return self.__phi / 10
