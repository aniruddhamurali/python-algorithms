'''Improved Euler's Method'''
def improved_eulers(xn, yn, h, finalx):
    approx = yn
    steps = int((finalx - xn)/h)

    tempx = xn
    tempy = yn

    for step in range(1, steps+1):
        m1 = f(tempx,tempy)
        m2 = f(tempx + h, tempy + h*m1)
        approx = tempy + h*(m1 + m2)/2

        tempx += h
        tempy = approx

    return approx


'''slope function - you can input this'''
def f(x, y):
    return (2*(y**2 + 1)/(x**2 + 4))
