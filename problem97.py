def solve_large_prime_digits():
    # Constants given in the problem
    multiplier = 28433
    base = 2
    exponent = 7830457
    addend = 1
    
    # We want the last 10 digits
    modulo = 10**10
    
    # Calculate (base^exponent) % modulo efficiently
    power_part = pow(base, exponent, modulo)
    
    # Calculate the final expression
    result = (multiplier * power_part + addend) % modulo
    
    # Return as a zero-padded string to ensure 10 digits are shown
    return f"{result:010d}"

if __name__ == "__main__":
    result = solve_large_prime_digits()
    print(f"The last ten digits of the prime number are: {result}")