"""
Utility functions for performing various projectile motion calculations
"""
from math import sqrt
from vector2d import Vector2D

g = Vector2D(9.8, -90)


def calculate_projectile_drop(velocity: Vector2D, time: float, acceleration=g) -> float:
    """

    :param velocity:
    :param time:
    :param acceleration:
    :return:
    """
    return velocity.y + 0.5 * acceleration.y * (time * time)


def calculate_time(height, acceleration=g) -> float:
    """

    :param height:
    :param acceleration:
    :return:
    """
    return sqrt(2 * height / acceleration.y)

def calculate_projectile_distance(velocity: Vector2D, height: float, acceleration=g) -> float:
    """

    :param velocity:
    :param height:
    :param acceleration:
    :return:
    """
    return velocity.x + acceleration.x * height / acceleration.y
