import math

def is_pentagonal(n):
    """Checks if a number n is pentagonal."""
    if n <= 0:
        return False
    # Inverse formula: n = (1 + sqrt(1 + 24*x)) / 6
    discriminant = 1 + 24 * n
    root = int(math.isqrt(discriminant))
    
    # Check if perfect square and satisfies divisibility
    if root * root != discriminant:
        return False
    return (1 + root) % 6 == 0

def solve_pentagon_numbers():
    k = 1
    while True:
        k += 1
        pk = k * (3 * k - 1) // 2
        
        # Iterate backwards to find the closest pairs first (heuristic)
        for j in range(k - 1, 0, -1):
            pj = j * (3 * j - 1) // 2
            
            diff = pk - pj
            
            # Check difference first as it is a stricter filter locally
            if is_pentagonal(diff):
                summ = pk + pj
                if is_pentagonal(summ):
                    return diff

if __name__ == "__main__":
    result = solve_pentagon_numbers()
    print(f"The value of D is: {result}")