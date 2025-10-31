import math
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0 and n != 2:
        return False
    start = int(math.sqrt(n))
    for i in range(3, start + 1, 2):
        if n % i == 0:
            return False
    return True
def calculate(limit):
    collect = []
    counter = [0] * limit
    for i in range(2, limit):
        if is_prime(i):
            collect.append(i)
    for prime in collect:
        print(prime)
        for j in range(prime,limit, prime):
            count = 0
            while j % prime == 0:
                j = j // prime
                count += 1
            counter[prime] = max(counter[prime],count)
            print(counter[prime])
    summing = 1
    for i in range(2, limit):
        summing *= (i ** counter[i])
    print(summing)
calculate(20)