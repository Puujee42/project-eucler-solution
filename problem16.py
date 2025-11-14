import time 
def binary_translate(power):
    result = []
    while power > 0:
        ans = power % 2
        result.append(ans)
        power //=2
    result.reverse()
    return result
def powering(power,base):
    result = 1
    i = len(power) -1
    while i >= 0:
        if power[i]  == 1:
            result *= base
        base*=base
        i-=1
    return result
def summer(value):
    result = 0
    while value > 0 :
        result += value%10
        value//=10
    return result
def calculate(power,base):
    power = binary_translate(power=power)
    print(power)
    result = powering(power,base)
    answer  =  summer(result)
    return answer
start = time.time()
result = calculate(1000,2)
end = time.time()
print(f"The answer is : {result}")
print(f"Calculation took: {end - start:.4f} seconds")