from Transform import *
import math


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def to_turn_oz(self, phi=0):
        turn = TurnOZ(phi=phi)
        self.x, self.y, self.z = turn * self

    def to_turn_ox(self, phi=0):
        turn = TurnOX(phi=phi)
        self.x, self.y, self.z = turn * self

    def to_turn_oy(self, phi=0):
        turn = TurnOY(phi=phi)
        self.x, self.y, self.z = turn * self

    def move(self, d_x=0, d_y=0, d_z=0):
        moving = Moving(d_x=d_x, d_y=d_y, d_z=d_z)
        self.x, self.y, self.z = moving * self

    def to_scale(self, k_x=0, k_y=0, k_z=0):
        scale = Scale(k_x=k_x, k_y=k_y, k_z=k_z)
        self.x, self.y, self.z = scale * self

    def to_orthographic_projection_z(self):
        orthographic_projection = OrthographicProjectionZ()
        self.x, self.y, self.z = orthographic_projection * self

    def to_orthographic_projection_x(self):
        orthographic_projection = OrthographicProjectionX()
        self.x, self.y, self.z = orthographic_projection * self

    def to_orthographic_projection_y(self):
        orthographic_projection = OrthographicProjectionY()
        self.x, self.y, self.z = orthographic_projection * self

    def to_isometric_transform(self, phi=-math.pi / 4, tetta=math.pi / 5):
        isometric_transform = IsometricTransform(phi=phi, tetta=tetta)
        self.x, self.y, self.z = isometric_transform * self
