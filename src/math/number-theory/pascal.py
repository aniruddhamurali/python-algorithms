# Generates an array of size n, displays Pascal's Triangle

def pascal(n):
    tri = [[1]]
    for i in range(1, n):
        start = [1]
        for n in range(0, i-1):
            start.append(tri[i-1][n]+tri[i-1][n+1])
        start.append(1)
        tri.append(start)
    return tri
