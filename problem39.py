def count_right_triangles(p):
    """Counts the number of integer right triangles with perimeter p."""
    count = 0
    # a must be less than p/3 because a < b < c and a+b+c = p implies 3a < p
    for a in range(1, p // 3):
        # From a^2 + b^2 = c^2 and a + b + c = p, we derive:
        # b = (p^2 - 2pa) / (2p - 2a)
        numerator = p * (p - 2 * a)
        denominator = 2 * (p - a)
        
        # Check if b is an integer
        if numerator % denominator == 0:
            count += 1
    return count

def solve():
    max_solutions = 0
    best_p = 0
    
    # Perimeter of integer right triangle is always even.
    # Iterate p from 12 (smallest is 3,4,5 -> p=12) up to 1000.
    for p in range(12, 1001, 2):
        solutions = count_right_triangles(p)
        if solutions > max_solutions:
            max_solutions = solutions
            best_p = p
            
    return best_p, max_solutions

if __name__ == "__main__":
    p_val, solutions = solve()
    print(f"The value of p that maximizes the number of solutions is: {p_val}")
    print(f"Number of solutions: {solutions}")