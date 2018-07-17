# This program calculates the derivative of a function at a point

# This is a function that you define
def f(x):
    return pow(x,2)

def derivative(f, *args):
    h = 1./10000000.
    slope = (f(*args[0]+h) - f(*args[0]))/h
    return slope

derivative(f, 3) # Example
