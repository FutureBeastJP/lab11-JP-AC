import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Error: Cannot take the square root of negative numbers.")
        raise

def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except (TypeError, ValueError) as e:
        print("Error: Invalid Input")
        raise

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b/a

def logarithm(a,b):
    if a<=0 or b<=0 or b ==1:
        raise ValueError("Invalid argument")
    return math.log(a,b)

def exponent(a,b):
    return a**b


