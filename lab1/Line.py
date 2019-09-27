class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, qp):
        qp.drawLine(self.start.getX(), self.start.getY(),
                    self.end.getX(), self.end.getY())
