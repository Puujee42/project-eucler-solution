import sys

def is_prime(n):
    """
    Checks if a number n is prime using trial division.
    This is efficient enough because n is roughly up to 700,000,000,
    so sqrt(n) is around 26,000.
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    side_length = 1
    prime_count = 0
    total_count = 1  # Represents the center number '1'
    
    # Loop indefinitely until the condition is met
    while True:
        side_length += 2
        
        # Calculate the values on the diagonals for the current layer.
        # Bottom Right corner is always a square s*s
        sq = side_length * side_length
        step = side_length - 1
        
        # The four corners are:
        # sq (Bottom Right - never prime)
        # sq - step (Bottom Left)
        # sq - 2*step (Top Left)
        # sq - 3*step (Top Right)
        
        c1 = sq - step
        c2 = sq - 2 * step
        c3 = sq - 3 * step
        
        if is_prime(c1): prime_count += 1
        if is_prime(c2): prime_count += 1
        if is_prime(c3): prime_count += 1
        
        # We add 4 new numbers to the diagonal count
        total_count += 4
        
        # Check if the ratio is below 10%
        if prime_count / total_count < 0.10:
            return side_length

if __name__ == "__main__":
    result = solve()
    print(f"Side length where ratio falls below 10%: {result}")