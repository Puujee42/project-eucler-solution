import math
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def calculate(val1,val2):
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
            print("No common prime factors")
        else:
            for container_val in container:
                print(container_val)
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
            print("No common prime factors")
        else:
            for container_val in container:
                print(container_val)
calculate(14,42)