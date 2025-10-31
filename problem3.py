import math
def calculate(limit):
    max_prime = -1
    while limit % 2 == 0:
        max_prime = 2
        limit = limit // 2
    for i in range(3, int(math.sqrt(limit)+1), 2):
        while limit % i == 0:
            max_prime = i
            limit = limit // i
    if limit > 2:
        max_prime = limit
    print(max_prime)
calculate(6008514751438)