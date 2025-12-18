def is_pentagonal(n):
    """
    Checks if a number n is a pentagonal number.
    Formula derived from P_k = k(3k-1)/2:
    k = (1 + sqrt(1 + 24n)) / 6
    """
    discriminant = 1 + 24 * n
    root = int(discriminant**0.5)
    
    # Check if discriminant is a perfect square
    if root * root != discriminant:
        return False
        
    # Check if k is a natural number
    return (1 + root) % 6 == 0

def solve_tri_pent_hex():
    # The problem gives H_143 = 40755. We start checking from m = 144.
    m = 144
    while True:
        # Generate Hexagonal number
        # Note: All hexagonal numbers are also triangle numbers.
        h_m = m * (2 * m - 1)
        
        if is_pentagonal(h_m):
            return h_m
            
        m += 1

if __name__ == "__main__":
    result = solve_tri_pent_hex()
    print(f"The next triangle number that is also pentagonal and hexagonal is: {result}")