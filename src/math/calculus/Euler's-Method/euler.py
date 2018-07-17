'''Euler's Method'''
def eulers(xn, yn, h, finalx):
    approx = yn
    steps = int((finalx - xn)/h)

    tempx = xn
    tempy = yn
    
    for step in range(1, steps+1):
        slope = f(tempx, tempy)
        approx = tempy + h*slope

        tempx += h
        tempy = approx

    return approx


'''slope function - you can input this'''
def f(x, y):
    return (2*(y**2 + 1)/(x**2 + 4))
