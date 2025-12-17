def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve_quadratic_primes():
    best_count = 0
    best_product = 0
    
    # b must be prime for n=0 to be prime.
    # We generate primes up to 1000.
    primes_for_b = [x for x in range(1001) if is_prime(x)]
    
    for b in primes_for_b:
        # |a| < 1000, so a ranges from -999 to 999
        for a in range(-999, 1000):
            
            # Optimization: 
            # For n=1, value is 1 + a + b.
            # If b > 2 (odd), then (1 + a + odd) = (even + a).
            # For result to be prime (odd), 'a' must be odd.
            # If b=2, a can be even.
            if b != 2 and a % 2 == 0:
                continue
                
            n = 0
            while True:
                value = n*n + a*n + b
                if not is_prime(value):
                    break
                n += 1
            
            if n > best_count:
                best_count = n
                best_product = a * b

    return best_product

if __name__ == "__main__":
    result = solve_quadratic_primes()
    print(f"The product of the coefficients a and b is: {result}")