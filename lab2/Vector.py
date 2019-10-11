from Point import Point


class Vector(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @classmethod
    def create_from_point(cls, start, end):
        point = end - start
        return cls(point.x, point.y, point.z)

    @staticmethod
    def calculate_scalar_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def calculate_cos_between_vectors(v1, v2):
        return Vector.calculate_scalar_product(v1, v2) / (v1.size * v2.size)

    @classmethod
    def create_normal(cls, p0, p1, p2):
        A = (p2.y - p0.y) * (p1.z - p0.z) - (p2.z - p0.z) * (p1.y - p0.y)
        B = (p2.z - p0.z) * (p1.x - p0.x) - (p2.x - p0.x) * (p1.z - p0.z)
        C = (p2.x - p0.x) * (p1.y - p0.y) - (p2.y - p0.y) * (p1.x - p0.x)
        return cls(A, B, C)

    @property
    def size(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1 / 2)
