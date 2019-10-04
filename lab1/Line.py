class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, qp):
        qp.drawLine(self.start.getX(), self.start.getY(),
                    self.end.getX(), self.end.getY())

    def to_turn(self, phi):
        self.start.to_turn(phi)
        self.end.to_turn(phi)

    def to_scale(self, k_x, k_y):
        self.start.to_scale(k_x, k_y)
        self.end.to_scale(k_x, k_y)

    def move(self, h, g):
        self.start.move(h, g)
        self.end.move(h, g)

    def move_x(self, h):
        self.start.move_x(h)
        self.end.move_x(h)

    def move_y(self, g):
        self.start.move_y(g)
        self.end.move_y(g)

    def __str__(self):
        return f'({self.start.x}; {self.start.y}) - ({self.end.x}; {self.end.y})'
