from copy import copy
from Vector import Vector
import math


class Plane:
    def __init__(self, lines, point1, point2, point3):
        self.list_line = [copy(i) for i in lines]
        self.point1 = copy(point1)
        self.point2 = copy(point2)
        self.point3 = copy(point3)
        self.normal = Vector.create_normal(
            self.point1, self.point2, self.point3)
        self.drawly = False

    def to_turn_oz(self, phi=0):
        self.point1.to_turn_oz(phi=phi)
        self.point2.to_turn_oz(phi=phi)
        self.point3.to_turn_oz(phi=phi)
        for i in range(len(self.list_line)):
            self.list_line[i].to_turn_oz(phi=phi)

    def to_turn_ox(self, phi=0):
        self.point1.to_turn_ox(phi=phi)
        self.point2.to_turn_ox(phi=phi)
        self.point3.to_turn_ox(phi=phi)
        for i in range(len(self.list_line)):
            self.list_line[i].to_turn_ox(phi=phi)

    def to_turn_oy(self, phi=0):
        self.point1.to_turn_oy(phi=phi)
        self.point2.to_turn_oy(phi=phi)
        self.point3.to_turn_oy(phi=phi)
        for i in range(len(self.list_line)):
            self.list_line[i].to_turn_oy(phi=phi)

    def move(self, d_x=0, d_y=0, d_z=0):
        self.point1.move(d_x=d_x, d_y=d_y, d_z=d_z)
        self.point2.move(d_x=d_x, d_y=d_y, d_z=d_z)
        self.point3.move(d_x=d_x, d_y=d_y, d_z=d_z)
        for i in range(len(self.list_line)):
            self.list_line[i].move(d_x=d_x, d_y=d_y, d_z=d_z)

    def to_scale(self, k_x=0, k_y=0, k_z=0):
        self.point1.to_scale(k_x=k_x, k_y=k_y, k_z=k_z)
        self.point2.to_scale(k_x=k_x, k_y=k_y, k_z=k_z)
        self.point3.to_scale(k_x=k_x, k_y=k_y, k_z=k_z)

        for i in range(len(self.list_line)):
            self.list_line[i].to_scale(k_x=k_x, k_y=k_y, k_z=k_z)

    def to_orthographic_projection_z(self):
        self.point1.to_orthographic_projection_z()
        self.point2.to_orthographic_projection_z()
        self.point3.to_orthographic_projection_z()

        for i in range(len(self.list_line)):
            self.list_line[i].to_orthographic_projection_z()

    def to_orthographic_projection_x(self):
        self.point1.to_orthographic_projection_x()
        self.point2.to_orthographic_projection_x()
        self.point3.to_orthographic_projection_x()

        for i in range(len(self.list_line)):
            self.list_line[i].to_orthographic_projection_x()

    def to_orthographic_projection_y(self):
        self.point1.to_orthographic_projection_y()
        self.point2.to_orthographic_projection_y()
        self.point3.to_orthographic_projection_y()

        for i in range(len(self.list_line)):
            self.list_line[i].to_orthographic_projection_y()

    def to_isometric_transform(self, phi=-math.pi / 4, tetta=math.pi / 5):
        self.point1.to_isometric_transform(phi=phi, tetta=tetta)
        self.point2.to_isometric_transform(phi=phi, tetta=tetta)
        self.point3.to_isometric_transform(phi=phi, tetta=tetta)

        for i in range(len(self.list_line)):
            self.list_line[i].to_isometric_transform(phi=phi, tetta=tetta)

    def clear(self, vector_see):
        self.normal = Vector.create_normal(
            self.point1, self.point2, self.point3)
        cos_VS_N = Vector.calculate_cos_between_vectors(
            vector_see, self.normal)
        if cos_VS_N > 0:
            self.drawly = True

    def __repr__(self):
        s = ''
        for i in range(len(self.list_line)):
            s += f'{self.list_line[i]}\n'
        return s

    def draw(self, qp):
        if self.drawly:
            for i in range(len(self.list_line)):
                self.list_line[i].draw(qp)
