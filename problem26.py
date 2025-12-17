def get_cycle_length(n):
    """Calculates the length of the recurring cycle of 1/n."""
    # Remove factors of 2 and 5 as they don't affect cycle length
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
        
    # If n becomes 1, it was a terminating decimal (e.g., 1/2, 1/4, 1/5, 1/10)
    if n == 1:
        return 0
    
    # Find smallest k such that 10^k % n == 1
    k = 1
    remainder = 10 % n
    
    while remainder != 1:
        remainder = (remainder * 10) % n
        k += 1
        
    return k

def solve_longest_cycle():
    max_length = 0
    result_d = 0
    
    # Iterate backwards from 999. 
    # Logic: The max cycle length for d is d-1. 
    # If we find a length L, and the next d we check is <= L, 
    # we can stop because no smaller d can produce a longer cycle.
    for d in range(999, 1, -1):
        if max_length >= d:
            break
            
        length = get_cycle_length(d)
        
        if length > max_length:
            max_length = length
            result_d = d
            
    return result_d

if __name__ == "__main__":
    result = solve_longest_cycle()
    print(f"The value of d < 1000 with the longest recurring cycle is: {result}")