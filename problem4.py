def pladindrome(num):
    string_num = str(num)
    if string_num == string_num[::-1]:
        return True
    return False
def calculate(limit):
    real_limit = 10 ** limit 
    print(real_limit)
    pair1 = (1,1)
    second = 10 ** (limit-1)
    max_palindrome = -1
    for i in range(second,real_limit):
        for j in range(i,real_limit):
            product = i * j
            if pladindrome(product):
                if(max_palindrome < product):
                    max_palindrome = product
                pair1 = (i,j)
    print(max_palindrome)
    print(pair1)
calculate(3)