import math
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def gcd(val1,val2):
    if val1 > val2:
        collect = []
        container = []
        for i in range(2,val1):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                val1 = val1 // prime
                val2 = val2 // prime
                container.append(prime)
        if len(container) == 0:
            print(1)
        else:
            ans = 1
            for container_val in container:
                ans *= container_val
            return ans
    else:
        collect = []
        container = []
        for i in range(2,val2):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                container.append(prime)
        if len(container) == 0:
            return 1
        else:
            ans = 1
            for prime in container:
                ans *= prime
            return ans
def lcm(val1,val2):
    if val1 > val2:
        collect = []
        container = []
        for i in range(2,val1):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                val1 = val1 // prime
                val2 = val2 // prime
                container.append(prime)
        if len(container) == 0:
            print(val1 * val2)
        else:
            ans = 1
            for container_val in container:
                ans *= container_val
            val = ans*val1*val2
    else:
        collect = []
        container = []
        for i in range(2,val2):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                val1 = val1 // prime
                val2 = val2 // prime
                container.append(prime)
        if len(container) == 0:
            print(val1 * val2)
        else:
            ans = 1
            for container_val in container:
                ans *= container_val
            val = ans*val1*val2
    return val
def euclid(val1,val2,val3):
    check = gcd(val1,val2)
    checker = gcd(val2,val3)
    if(check == checker):
        return True
    else:
        return False
def calculate():
    val1 = int(input("Enter first value:"))
    val2 = int(input("Enter second value:"))
    print(gcd(val1,val2))
    print(euclid(95,25,20))
calculate()