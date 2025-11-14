def is_prime(n):
    if n % 2 ==0 and n > 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i ==0:
            return False
    return True
def calculate(value1):
    prime_list = []
    count = 0
    i = 2
    while count < value1:
        if(is_prime(i)):
            count = count + 1
            prime_list.append(i)
        i = i + 1
    return i - 1
print(calculate(10001))