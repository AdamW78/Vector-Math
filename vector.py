"""
Class containing Vector representation and helper methods
"""
from math import sin, cos, radians, sqrt, atan, degrees

EPSILON = 1e-15
DEBUG = False


class Vector:
    """
    Class representing a 2-dimensional vector.
    """

    def __init__(self, magnitude, direction):
        self.magnitude = float(magnitude)
        self.x = cos(radians(direction))
        self.x = 0.0 if self.x < EPSILON else self.x * self.magnitude
        self.y = sin(radians(direction)) * magnitude
        self.y = 0.0 if self.y < EPSILON else self.y * self.magnitude

        self.direction = float(direction)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.update_vector()

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.update_vector()

    def __repr__(self):
        return (f"Vector(Magnitude: {self.magnitude}, Direction: {self.direction}, "
                f"X-Component: {self.x}, Y-Component: {self.y})")

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Vector):
            mag_eq = abs(self.magnitude - other.magnitude) < EPSILON
            direction_eq = abs(self.direction - other.direction) < EPSILON
            x_eq = abs(self.x - other.x) < EPSILON
            y_eq = abs(self.y - other.y) < EPSILON
            if DEBUG:
                print(f"About to perform equality checks between two vectors:\n{self}\n{other}")
                print(f"Equality Evaluations:\nMagnitude: {mag_eq}, Direction: {direction_eq}, "
                      f"X-Components: {x_eq}, Y-Components: {y_eq}")
            return mag_eq and direction_eq and x_eq and y_eq
        return False

    def update_vector(self):
        """
        Updates a vector's magnitude and direction based on its x and y components.
        :return:
        """
        self.update_magnitude()
        self.update_direction()

    def update_magnitude(self):
        """
        Updates the magnitude of the vector based on its x and y components.
        """
        self.magnitude = sqrt(self.x * self.x + self.y * self.y)

    def update_direction(self):
        """
        Updates the direction of the vector based on its x and y components.
        """
        if self.x == 0:
            self.direction = 90.0 if self.y > 0 else -90.0
        else:
            self.direction = degrees(atan(self.y / self.x))

    def scalar_multiply(self, scalar):
        """
        Perform scalar multiplication on a Vector
        :param scalar: Scalar by which to multiply the vector
        """
        self.magnitude *= scalar
        self.x *= scalar
        self.y *= scalar


def create_from_components(x: float, y: float) -> Vector:
    """
    Create a Vector from x and y components.
    :param x: X component of vector.
    :param y: Y component of vector.
    :return: Vector instance
    """
    vec = Vector(0, 0)
    vec.x = float(x)
    vec.y = float(y)
    vec.update_vector()
    return vec


v = Vector(1, 45)
v_a = create_from_components(sqrt(2) / 2, sqrt(2) / 2)
DEBUG = True
print(f"Vectors v and v_a are equal: {v == v_a}")
