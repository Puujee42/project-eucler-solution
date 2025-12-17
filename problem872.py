def solve():
    # The problem likely refers to 10^17 and 9^17 based on Project Euler #872
    # If you strictly meant 1017 and 917, you can change these values.
    N = 10**17
    K = 9**17

    # f(N, K) is the sum of nodes on the path from K to N.
    # The path consists of nodes obtained by adding the largest power of 2 
    # that fits within the difference to N.
    
    diff = N - K
    if diff < 0:
        print("K must be less than or equal to N")
        return

    # Find the positions of all set bits in the difference
    # These bits correspond to the steps ("jumps") between nodes in the path.
    bits = []
    temp = diff
    pos = 0
    while temp > 0:
        if temp & 1:
            bits.append(pos)
        temp >>= 1
        pos += 1
    
    # Sort bits from Most Significant to Least Significant (Descending)
    bits.sort(reverse=True)
    
    
    m = len(bits)
    total_sum = (m + 1) * N
    
    subtraction_term = 0
    for i, b in enumerate(bits):
        rank = i + 1
        subtraction_term += rank * (1 << b)
        
    result = total_sum - subtraction_term
    
    print(f"f(10^17, 9^17) = {result}")

if __name__ == "__main__":
    solve()