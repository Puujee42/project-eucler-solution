import time
def collatz(x):
    collection = [0] * (x+1)
    maxed = 0
    result = 0
    for i in range(1,x):
        count = 0
        val = i
        while val > 1:
            if val % 2 != 0:
                count +=1
                val = val*3 + 1
            else:
                count += 1
                val //=2
            if val < i:
                if collection[val] > 0:
                    count = count + collection[val]
                    break
        collection[i] = count
        if maxed < collection[i]:
            maxed = collection[i]
            result = i
    return result
def calculate():
    x = collatz(10000001)
    return x
start_time = time.time()
result = calculate()
end_time = time.time()
print(f"The number with the longest chain is: {calculate()}")
print(f"Calculation took: {end_time - start_time:.4f} seconds")