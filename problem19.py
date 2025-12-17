def calculate(x):
    n = 1
    s = 1
    for i in range(0,x):
        n += 1
        s *= n
    print(s)
    res = 0
    while s > 0 :
        res += s % 10
        s //= 10
        
    return res
print(calculate(99))