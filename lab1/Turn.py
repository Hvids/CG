class Turn:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.__turn = 0

    def update_turn(self):
        self.__turn += (self.end - self.start)

    def get_turn(self):
        return self.__turn
