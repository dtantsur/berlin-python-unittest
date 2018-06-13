import math


def roots(a, b, c):
    if not a:
        raise ValueError("a cannot be zero")

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise ValueError("discriminant below zero")

    return ((- b - math.sqrt(discriminant)) / 2 / a,
            (- b + math.sqrt(discriminant)) / 2 / a)
