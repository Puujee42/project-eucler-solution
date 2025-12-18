import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def is_s_number(n, target):
    """
    Recursively checks if the number n can be split into parts that sum to target.
    """
    # Base case: if the remaining number equals the target, we found a valid split.
    if n == target:
        return True
    
    # Pruning: The sum of parts of n is always <= n. 
    # If n < target, we can never reach the target.
    if n < target:
        return False
    
    # Try splitting n at different positions
    # We iterate through powers of 10 to split n into (left, right)
    m = 10
    while m <= n:
        right = n % m
        left = n // m
        
        # Optimization: The current part (right) cannot exceed the target.
        if right < target:
            # Recursively check if the left part can sum to the remaining target
            if is_s_number(left, target - right):
                return True
        
        m *= 10
        
    return False

def solve():
    # Define the limit. 
    # Standard PE 719 is 10^12. 
    # Note: 10^16 requires iterating up to 10^8, which may take several minutes in Python.
    N = 10**12 
    limit = int(N**0.5)
    
    total_sum = 0
    
    print(f"Calculating T({N})...")
    
    # Iterate through all square roots i
    for i in range(2, limit + 1):
        # Optimization:
        # If n = i^2 is an S-number, then sum(parts) = i.
        # We know n == sum(parts) (mod 9).
        # Therefore, i^2 == i (mod 9) => i^2 - i == 0 (mod 9) => i(i-1) == 0 (mod 9).
        # This implies i % 9 must be 0 or 1.
        if i % 9 <= 1:
            square = i * i
            
            # Check if the square can be split to sum to i.
            # The function handles the "2 or more numbers" constraint implicitly
            # because 'square' > 'i' (for i > 1), so the base case n==target
            # is never met immediately; it forces at least one split.
            if is_s_number(square, i):
                total_sum += square
                
    print(f"The sum T({N}) is: {total_sum}")

if __name__ == "__main__":
    solve()