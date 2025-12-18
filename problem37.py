import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def solve_truncatable_primes():
    # Step 1: Generate Right-Truncatable Primes
    # We start with the single digit primes
    queue = [2, 3, 5, 7]
    candidates = [] # This will store right-truncatable primes > 9
    
    while queue:
        current = queue.pop(0)
        
        # Try appending odd digits (except 5) to keep it potentially prime
        for digit in [1, 3, 7, 9]:
            next_val = current * 10 + digit
            if is_prime(next_val):
                queue.append(next_val)
                candidates.append(next_val)
    
    # Step 2: Filter for Left-Truncatable Primes
    truncatable_primes = []
    
    for p in candidates:
        s_p = str(p)
        is_left_truncatable = True
        
        # Check all suffixes
        # s_p[1:] removes the first digit, s_p[2:] removes first two, etc.
        for i in range(1, len(s_p)):
            if not is_prime(int(s_p[i:])):
                is_left_truncatable = False
                break
        
        if is_left_truncatable:
            truncatable_primes.append(p)
            
    # Step 3: Return the sum
    return sum(truncatable_primes)

if __name__ == "__main__":
    result = solve_truncatable_primes()
    print(f"The sum of the eleven truncatable primes is: {result}")