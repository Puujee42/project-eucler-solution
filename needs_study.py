import time

def count_divisors(n):
    """
    Calculates the number of divisors of 'n' using its prime factorization.
    This is the core of the optimization.
    
    Example: n = 28 -> 2^2 * 7^1
    Divisors = (2 + 1) * (1 + 1) = 6
    """
    if n == 1:
        return 1
    
    num_divisors = 1
    
    # First, handle the prime factor '2'
    power = 0
    while n % 2 == 0:
        power += 1
        n //= 2
    if power > 0:
        num_divisors *= (power + 1) # This is the (a₁ + 1) part of the formula
        
    # Now, handle the odd prime factors
    p = 3
    while p * p <= n:
        power = 0
        while n % p == 0:
            power += 1
            n //= p
        if power > 0:
            num_divisors *= (power + 1) # This is for (a₂ + 1), (a₃ + 1), etc.
        p += 2
        
    # If 'n' is still greater than 1, it must be a prime factor itself
    if n > 1:
        num_divisors *= 2 # Corresponds to a power of 1, so (1 + 1)
        
    return num_divisors

def find_triangular_number(target_divisors):
    """
    Finds the first triangular number with more than 'target_divisors'.
    
    It uses the property that Tn = n * (n+1) / 2 and that n and n+1 are coprime.
    This allows us to calculate divisors for two smaller numbers instead of one huge one.
    """
    n = 1
    num_divs_n1 = 1      # Stores the number of divisors for one part
    num_divs_n2 = 1      # Stores the number of divisors for the other part
    
    while True:
        # We leverage that n and n+1 are coprime. So, the number of divisors
        # of their product is the product of their individual number of divisors.
        if n % 2 == 0:
            # Case 1: Tn = (n/2) * (n+1)
            num_divs_n1 = count_divisors(n // 2)
            num_divs_n2 = count_divisors(n + 1)
        else:
            # Case 2: Tn = n * ((n+1)/2)
            num_divs_n1 = count_divisors(n)
            num_divs_n2 = count_divisors((n + 1) // 2)
            
        total_divisors = num_divs_n1 * num_divs_n2
        
        if total_divisors > target_divisors:
            # We found it! Calculate the final triangular number and return it.
            return n * (n + 1) // 2
            
        # Move to the next number in the sequence
        n += 1

# --- Main execution ---
start_time = time.time()
target = 500
result = find_triangular_number(target)
end_time = time.time()

print(f"The first triangular number to have over {target} divisors is: {result}")
print(f"Calculation took: {end_time - start_time:.4f} seconds")