"""
Class containing Vector representation and helper methods
"""
from math import sin, cos, radians, sqrt, atan, degrees

EPSILON = 1e-15
DEBUG = False


class Vector2D:
    """
    Class representing a 2-dimensional vector.
    """

    def __init__(self, magnitude, direction):
        self.magnitude = float(magnitude)
        self.x = cos(radians(direction))
        self.x = 0.0 if abs(self.x) < EPSILON else self.x * self.magnitude
        self.y = sin(radians(direction))
        self.y = 0.0 if abs(self.y) < EPSILON else self.y * self.magnitude
        self.direction = float(direction)
        print(f"Vector2D initialized with magnitude {self.magnitude}, direction {direction}\n"
              f"X-Component: {self.x}, Y-Component: {self.y}")

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return create_from_components(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return create_from_components(x, y)

    def __repr__(self):
        return (f"Vector(Magnitude: {self.magnitude}, Direction: {self.direction}, "
                f"X-Component: {self.x}, Y-Component: {self.y})")

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Vector2D):
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


def create_from_components(x: float, y: float) -> Vector2D:
    """
    Create a Vector from x and y components.
    :param x: X component of vector.
    :param y: Y component of vector.
    :return: Vector instance
    """
    vec = Vector2D(0, 0)
    vec.x = float(x)
    vec.y = float(y)
    vec.update_vector()
    return vec


v = Vector2D(4.9, 31.5)
v_1 = Vector2D(6.3, -60)
v_2 = v_1 - v
print(f"Subtracting vector {v} from vector {v_1}...")
print(f"Got result: {v_2}")
print(f"Per second (given vector time of 2 seconds), x: {v_2.x/2}, y: {v_2.y/2}")
