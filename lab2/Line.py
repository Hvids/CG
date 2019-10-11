from copy import copy
import math


class Line:
    def __init__(self, start, end):
        self.start = copy(start)
        self.end = copy(end)

    def __repr__(self):
        return f"({self.start.x}, {self.start.y},{self.start.z}) - ({self.end.x}, {self.end.y},{self.end.z})"

    def __str__(self):
        return f"({self.start.x}, {self.start.y},{self.start.z}) - ({self.end.x}, {self.end.y},{self.end.z})"

    def draw(self, qp):
        qp.drawLine(self.start.x, self.start.y, self.end.x, self.end.y)

    def to_turn_oz(self, phi=0):
        self.start.to_turn_oz(phi=phi)
        self.end.to_turn_oz(phi=phi)

    def to_turn_ox(self, phi=0):
        self.start.to_turn_ox(phi=phi)
        self.end.to_turn_ox(phi=phi)

    def to_turn_oy(self, phi=0):
        self.start.to_turn_oy(phi=phi)
        self.end.to_turn_oy(phi=phi)

    def move(self, d_x=0, d_y=0, d_z=0):
        self.start.move(d_x=d_x, d_y=d_y, d_z=d_z)
        self.end.move(d_x=d_x, d_y=d_y, d_z=d_z)

    def to_scale(self, k_x=0, k_y=0, k_z=0):
        self.start.to_scale(k_x=k_x, k_y=k_y, k_z=k_z)
        self.end.to_scale(k_x=k_x, k_y=k_y, k_z=k_z)

    def to_orthographic_projection_z(self):
        self.start.to_orthographic_projection_z()
        self.end.to_orthographic_projection_z()

    def to_orthographic_projection_x(self):
        self.start.to_orthographic_projection_x()
        self.end.to_orthographic_projection_x()

    def to_orthographic_projection_y(self):
        self.start.to_orthographic_projection_y()
        self.end.to_orthographic_projection_y()

    def to_isometric_transform(self, phi=-math.pi / 4, tetta=math.pi / 5):
        self.start.to_isometric_transform(phi=phi, tetta=tetta)
        self.end.to_isometric_transform(phi=phi, tetta=tetta)
