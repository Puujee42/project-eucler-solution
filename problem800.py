import math

def get_primes(n):
    """ Returns a list of primes < n using Sieve of Eratosthenes """
    # Sieve array for odd numbers
    sieve = bytearray([1]) * ((n + 1) // 2)
    sieve[0] = 0 
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i // 2 :: i] = bytearray((n - i*i - 1) // (2 * i) + 1)
    return [2] + [2*i + 1 for i in range(1, (n + 1) // 2) if sieve[i]]

def solve():
    BASE = 800800
    # Target value L = ln(N) = BASE * ln(BASE)
    limit_val = BASE * math.log(BASE)
    
    # Estimate upper bound for primes: q * ln(2) < L
    max_q = int(limit_val / math.log(2)) + 5000
    
    primes = get_primes(max_q)
    # Precompute logs to speed up the loop
    primes_log = [math.log(p) for p in primes]
    
    count = 0
    n_primes = len(primes)
    right = n_primes - 1
    
    for left in range(n_primes):
        p = primes[left]
        log_p = primes_log[left]
        
        # We enforce p < q. If left >= right, p >= q, so stop.
        if left >= right:
            break
            
        # Move right pointer to the left until condition is met
        while right > left:
            q = primes[right]
            log_q = primes_log[right]
            
            # Check p^q * q^p <= N  <=>  q*ln(p) + p*ln(q) <= L
            if q * log_p + p * log_q <= limit_val:
                break
            right -= 1
        
        # If no q > p satisfies the condition, then for larger p no q will satisfy either (heuristic, but loop condition handles it)
        if right <= left:
            break
            
        # All primes from index left+1 to right are valid q's
        count += (right - left)
        
    return count

if __name__ == "__main__":
    print(solve())