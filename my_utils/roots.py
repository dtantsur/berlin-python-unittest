import math
import sys


def roots(a, b, c):
    if not a:
        raise ValueError("a cannot be zero")

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise ValueError("discriminant below zero")

    return ((- b - math.sqrt(discriminant)) / 2 / a,
            (- b + math.sqrt(discriminant)) / 2 / a)


def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
    except IndexError:
        sys.exit('3 arguments required')
    except ValueError:
        sys.exit('all arguments must be integers')
    print(roots(a, b, c))


if __name__ == '__main__':
    main()
