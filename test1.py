def solver(a,m,r):
    i = 1
    result = m*i+r
    print(result)
    while result % a > 0:
        i = i + 1
        result = m * i + 1
    return result
def calculate(a,m,r):
    result = solver(a,m,r) // a
    return result
print(calculate(7,6 ,1))