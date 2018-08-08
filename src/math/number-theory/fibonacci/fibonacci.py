def fibonacci(n):
    '''fibonacci(int) -> int
    Returns the nth Fibonacci number.'''
    fibList = [0,1,1] 
    for m in range(3,n+1): 
        newFib = fibList[m-1] + fibList[m-2]  
        fibList.append(newFib)
    return fibList[n]
