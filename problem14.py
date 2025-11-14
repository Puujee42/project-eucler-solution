def calculate(x):
    x = x * 2
    pictorial  = [0]*(x+1)
    pictorial[1] = 1 
    pictorial[0] = 1
    for i in range(2,x+1):
        pictorial[i] = pictorial[i-1]*i
    n = x // 2
    result = pictorial[x]//(pictorial[n]**2)
    return result
print(calculate(20))