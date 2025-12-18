import itertools

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

def solve_largest_pandigital_prime():
    # Digits for 7-digit pandigital numbers
    digits = '7654321'
    
    # Generate permutations in lexicographical order (descending because input is descending)
    # Since input is '7654321', itertools.permutations generates them in descending order automatically
    for p in itertools.permutations(digits):
        # Join tuple to string, then convert to integer
        num_str = "".join(p)
        num = int(num_str)
        
        # Optimization: Last digit must be odd and not 5 (i.e., 1, 3, 7)
        # Note: '5' is impossible at end for pandigital of length 7 avoiding divisibility by 5? 
        # Actually any number ending in 5 is div by 5.
        # Digits are 1..7. Evens are 2,4,6. 5 is 5. 
        # So last digit must be 1, 3, or 7.
        last_digit = num_str[-1]
        if last_digit in '2456':
            continue
            
        if is_prime(num):
            return num
            
    return None

if __name__ == "__main__":
    result = solve_largest_pandigital_prime()
    print(f"The largest n-digit pandigital prime is: {result}")