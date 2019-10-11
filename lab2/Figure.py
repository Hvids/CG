from Point import Point
from Line import Line
from Plane import Plane
import math


class Figure:
    def __init__(self):
        self.planes = []

    def to_turn_oz(self, phi=0):
        for i in range(len(self.planes)):
            self.planes[i].to_turn_oz(phi=phi)

    def to_turn_ox(self, phi=0):
        for i in range(len(self.planes)):
            self.planes[i].to_turn_ox(phi=phi)

    def to_turn_oy(self, phi=0):
        for i in range(len(self.planes)):
            self.planes[i].to_turn_oy(phi=phi)

    def move(self, d_x=0, d_y=0, d_z=0):
        for i in range(len(self.planes)):
            self.planes[i].move(d_x=d_x, d_y=d_y, d_z=d_z)

    def to_scale(self, k_x=0, k_y=0, k_z=0):
        for i in range(len(self.planes)):
            self.planes[i].to_scale(k_x=k_x, k_y=k_y, k_z=k_z)

    def to_orthographic_projection_z(self):
        for i in range(len(self.planes)):
            self.planes[i].to_orthographic_projection_z()

    def to_orthographic_projection_x(self):
        for i in range(len(self.planes)):
            self.planes[i].to_orthographic_projection_x()

    def to_orthographic_projection_y(self):
        for i in range(len(self.planes)):
            self.planes[i].to_orthographic_projection_y()

    def to_isometric_transform(self, phi=-math.pi / 4, tetta=math.pi / 5):
        for i in range(len(self.planes)):
            self.planes[i].to_isometric_transform(phi=phi, tetta=tetta)

    def clear(self, vector_see):
        for i in range(len(self.planes)):
            self.planes[i].clear(vector_see)

    def draw(self, qp):
        for i in range(len(self.planes)):
            self.planes[i].draw(qp)
