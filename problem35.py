def solve_circular_primes():
    limit = 1000000
    
    # Step 1: Sieve of Eratosthenes to find primes up to 1 million
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
                
    # Convert to a set for O(1) lookups
    primes = set(i for i, is_prime in enumerate(sieve) if is_prime)
    
    count = 0
    
    # Step 2: Iterate through primes and check circular property
    for p in primes:
        s = str(p)
        
        # Optimization: Filter out multi-digit numbers containing even digits or 5.
        # If a number has '0', '2', '4', '6', '8', or '5', one of its rotations 
        # will end in that digit, making it composite (divisible by 2 or 5).
        # We skip this check for single-digit primes (2, 3, 5, 7).
        if len(s) > 1:
            if any(c in '024568' for c in s):
                continue
        
        # Step 3: Check all rotations
        is_circular = True
        # We rotate len(s) - 1 times (since the 0th rotation is the number itself, already checked)
        for i in range(1, len(s)):
            # Create rotation: move first character to the end
            s = s[1:] + s[0]
            if int(s) not in primes:
                is_circular = False
                break
        
        if is_circular:
            count += 1
            
    return count

if __name__ == "__main__":
    result = solve_circular_primes()
    print(f"The number of circular primes below one million is: {result}")