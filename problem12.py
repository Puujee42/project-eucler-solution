def primer(n):
    count = 0
    result = 1
    if n == 1:
        return 1
    while n % 2 == 0:
        count = count + 1
        n //=2
    if count > 0:
        result *=(count)+1
    p = 3
    while p*p <= n:
        power = 0
        while n % p == 0:
            power= power + 1
            n//=p
        if power  > 0:
            result*=(power+1)
        p += 2
    if(n > 1):
        result *= 2
    return result
def triangle(x):
    n = 1
    num_div1 = 1
    num_div2 = 1
    while True:
        if n % 2 == 0:
            num_div1 = primer(n // 2)
            num_div2 = primer(n+1)
        else:
            num_div1 = primer(n)
            num_div2 = primer((n+1)//2)
        if num_div1 * num_div2 > x:
            return n*(n+1)//2
        n = n + 1
def calculate(x):
    result = triangle(x)
    return result
print(calculate(500))