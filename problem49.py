def solve_prime_permutations():
    # Sieve of Eratosthenes to find primes up to 10000
    limit = 10000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
    
    # Only interested in 4-digit primes
    primes = [i for i in range(1000, limit) if is_prime[i]]
    primes_set = set(primes)
    
    difference = 3330
    
    for p1 in primes:
        # Optimization: p1 must be less than 10000 - 6660 = 3340
        if p1 >= 3340:
            break
            
        p2 = p1 + difference
        p3 = p2 + difference
        
        # Check if p2 and p3 are prime
        if p2 in primes_set and p3 in primes_set:
            # Check if they are permutations of each other
            s1 = sorted(str(p1))
            s2 = sorted(str(p2))
            s3 = sorted(str(p3))
            
            if s1 == s2 and s2 == s3:
                # We found a sequence. Exclude the example given in the problem.
                if p1 != 1487:
                    return f"{p1}{p2}{p3}"

if __name__ == "__main__":
    result = solve_prime_permutations()
    print(f"The 12-digit number is: {result}")