import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if b <= 0 or b == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if a <= 0:
        raise ValueError("Argument must be positive")
    return math.log(a, b)


def exp(a, b):
    return a ** b


def hypotenuse(a, b):
    return math.hypot(a, b)


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)