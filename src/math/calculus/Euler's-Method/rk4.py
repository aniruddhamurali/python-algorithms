'''Fourth Order Runge-Kutta Method (RK4)'''
def rk4(xn, yn, h, finalx):
    approx = yn
    steps = int((finalx - xn)/h)

    tempx = xn
    tempy = yn

    for step in range(1, steps+1):
        k1 = h*f(tempx, tempy)
        k2 = h*f(tempx + k1/2, tempy + h/2)
        k3 = h*f(tempx + k2/2, tempy + h/2)
        k4 = h*f(tempx + k3, tempy + h)
        approx = tempy + (k1 + 2*k2 + 2*k3 + k4)/6

        tempx += h
        tempy = approx

    return approx



'''slope function - you can input this'''
def f(x, y):
    return (2*(y**2 + 1)/(x**2 + 4))
