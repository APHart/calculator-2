"""Math functions for calculator."""


def add(num_list):
    """Return the sum of a list of numbers."""

    total = 0
    for num in num_list:
        total += num

    return total


def subtract(num_list):
    """Return the second number subtracted from the first."""

    total = num_list[0]
    for num in num_list:
        total -= num

    return total


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    return num1 ** 2


def cube(num1):
    """Return the cube of the input."""

    return num1 ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2


def add_mult(num1, num2, num3):
    """Returns the product of the sum of num1 and num2 multiplied by num3."""

    return (num1 + num2) * num3


def add_cubes(num1, num2):
    """Returns the sum of the cube of num1 and the cube of num2."""

    return (num1 ** 3) + (num2 ** 3)
