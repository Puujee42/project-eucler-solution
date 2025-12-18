import math

def count_large_combinations():
    limit = 1000000
    total_count = 0
    
    # We iterate n from 1 to 100
    for n in range(1, 101):
        # We only need to check r up to n/2 due to symmetry.
        # Once we find the first r where nCr > limit, we can calculate the rest.
        for r in range(n // 2 + 1):
            if math.comb(n, r) > limit:
                # Based on symmetry, values > limit range from r to n-r.
                # The number of terms is (n - r) - r + 1
                total_count += (n - 2 * r + 1)
                
                # Once we find the first satisfying r for this n, we stop checking r
                # and move to the next n.
                break
                
    return total_count

if __name__ == "__main__":
    result = count_large_combinations()
    print(f"The number of values of nCr greater than one million is: {result}")