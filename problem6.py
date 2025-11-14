def calculate(value1,value2):
    n = (value2 - value1)+1
    square_ans = ((n*(n+1))//2)**2
    ans_square = (n*(n+1)*(2*n+1))//6
    result = square_ans - ans_square
    return result
print(calculate(1,100))