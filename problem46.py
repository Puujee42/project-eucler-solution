import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve_goldbach_other_conjecture():
    # Start checking from the first odd composite number
    n = 9
    
    while True:
        # We are looking for odd COMPOSITE numbers
        if not is_prime(n):
            satisfies_conjecture = False
            k = 1
            
            # Check n = p + 2*k^2
            # We iterate k. The maximum 2*k^2 must be less than n (since p must be at least 2)
            while 2 * k * k < n:
                remainder = n - 2 * k * k
                
                if is_prime(remainder):
                    satisfies_conjecture = True
                    break
                k += 1
            
            # If the loop finishes and we haven't found a valid representation
            if not satisfies_conjecture:
                return n
        
        # Check the next odd number
        n += 2

if __name__ == "__main__":
    result = solve_goldbach_other_conjecture()
    print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is: {result}")