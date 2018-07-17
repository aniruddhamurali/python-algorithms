# Calculates the integral of a function from startX to endX

# This is a function you define
def f(x):
    return pow(x,2)


def integral(startX, endX, numRect):
    width = (endX - startX)/numRect
    total = 0
    for i in range(1,numRect):
      height = f(startX + i * width)
      area = height * width
      total += area
    return total
