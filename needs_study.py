import time

def count_divisors(n):
    """
    Calculates the number of divisors of 'n' using its prime factorization.
    This function is already efficient and correct.
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
        num_divisors *= (power + 1)
        
    # Now, handle the odd prime factors
    p = 3
    while p * p <= n:
        power = 0
        while n % p == 0:
            power += 1
            n //= p
        if power > 0:
            num_divisors *= (power + 1)
        p += 2
        
    # If 'n' is still greater than 1, it must be a prime factor itself
    if n > 1:
        num_divisors *= 2
        
    return num_divisors

def find_triangular_number(target_divisors):
    """
    Finds the first triangular number with more than 'target_divisors'.
    The core logic remains the same, but with an added progress indicator.
    """
    n = 1
    max_divs_found = 0
    
    while True:
        # We leverage that n and n+1 are coprime. This allows us to calculate
        # divisors for two smaller numbers instead of one very large one.
        if n % 2 == 0:
            num_divs_n1 = count_divisors(n // 2)
            num_divs_n2 = count_divisors(n + 1)
        else:
            num_divs_n1 = count_divisors(n)
            num_divs_n2 = count_divisors((n + 1) // 2)
            
        total_divisors = num_divs_n1 * num_divs_n2
        
        # Keep track of the highest number of divisors found so far
        if total_divisors > max_divs_found:
            max_divs_found = total_divisors

        # === FIX: Added a progress indicator ===
        # This reassures you that the script is working and has not frozen.
        # It prints the status every 1000 iterations.
        if n % 1000 == 0:
            print(f"Searching... currently at n={n}, max divisors found so far: {max_divs_found}")

        if total_divisors > target_divisors:
            # We found the solution!
            print(f"\n--- Solution Found! ---")
            print(f"At n = {n}, found a total of {total_divisors} divisors.")
            return n * (n + 1) // 2
            
        # Move to the next number in the sequence
        n += 1

# --- Main execution ---
start_time = time.time()
target = 1000
result = find_triangular_number(target)
end_time = time.time()

print(f"\nThe first triangular number to have over {target} divisors is: {result}")
print(f"Calculation took: {end_time - start_time:.4f} seconds")