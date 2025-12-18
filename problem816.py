import sys
import math

# Increase recursion limit for deep recursion in Divide & Conquer
sys.setrecursionlimit(100000)

def generate_points(k):
    """
    Generates k points based on the Linear Congruential Generator.
    """
    s0 = 290797
    mod = 50515093
    
    # We need 2*k values of s sequence for k points
    limit = 2 * k
    s_values = [0] * limit
    
    curr = s0
    s_values[0] = curr
    for i in range(1, limit):
        curr = (curr * curr) % mod
        s_values[i] = curr
        
    points = []
    for i in range(k):
        # P_n = (s_2n, s_2n+1)
        points.append((s_values[2*i], s_values[2*i+1]))
        
    return points

def dist_sq(p1, p2):
    """Calculates squared Euclidean distance to avoid slow sqrt calls."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def brute_force_closest(points):
    """O(N^2) fallback for small lists."""
    min_d2 = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d2 = dist_sq(points[i], points[j])
            if d2 < min_d2:
                min_d2 = d2
    return min_d2

def closest_pair_rec(points_sorted_x):
    """
    Recursive Divide and Conquer function.
    Returns the squared minimum distance.
    """
    n = len(points_sorted_x)
    
    # Base case: for small number of points, use brute force
    if n <= 3:
        return brute_force_closest(points_sorted_x)
    
    # Divide
    mid = n // 2
    mid_point = points_sorted_x[mid]
    
    left_half = points_sorted_x[:mid]
    right_half = points_sorted_x[mid:]
    
    # Conquer
    d2_left = closest_pair_rec(left_half)
    d2_right = closest_pair_rec(right_half)
    
    # Current minimum squared distance
    min_d2 = min(d2_left, d2_right)
    
    # Check the "strip" (points close to the dividing line)
    # We only care about points where (x - mid_x)^2 < min_d2
    mid_x = mid_point[0]
    strip = []
    for p in points_sorted_x:
        if (p[0] - mid_x)**2 < min_d2:
            strip.append(p)
            
    # Sort strip by Y coordinate to limit comparisons
    strip.sort(key=lambda p: p[1])
    
    # Scan strip: theoretically we only need to check next 7 points
    strip_len = len(strip)
    for i in range(strip_len):
        for j in range(i + 1, strip_len):
            p1 = strip[i]
            p2 = strip[j]
            
            # If Y difference squared is already larger than min_d2, stop checking neighbors
            if (p1[1] - p2[1])**2 >= min_d2:
                break
                
            d2 = dist_sq(p1, p2)
            if d2 < min_d2:
                min_d2 = d2
                
    return min_d2

def solve_pure_python(k):
    print(f"Generating {k} points...")
    points = generate_points(k)
    
    print("Sorting points by X coordinate...")
    # Pre-sort by X is required for the D&C algorithm
    points.sort(key=lambda p: p[0])
    
    print("Calculating shortest distance (this may take a minute)...")
    min_d2 = closest_pair_rec(points)
    
    return math.sqrt(min_d2)

def main():
    # --- Verification ---
    print("--- Verifying Example Case d(14) ---")
    pts_14 = generate_points(14)
    # Using brute force for verification
    d2_14 = brute_force_closest(pts_14)
    d_14 = math.sqrt(d2_14)
    print(f"d(14) Result: {d_14:.9f}")
    print(f"Expected:     546446.466846479")
    
    if abs(d_14 - 546446.466846479) < 1e-6:
        print("Verification Passed.\n")
    else:
        print("Verification Failed.\n")
        return

    # --- Solution ---
    print("--- Solving for d(2,000,000) ---")
    # This runs in O(N log^2 N) or O(N log N) depending on strip density.
    # For random points, this is very efficient.
    result = solve_pure_python(2000000)
    
    print("-" * 30)
    print(f"Final Answer: {result:.9f}")
    print("-" * 30)

if __name__ == "__main__":
    main()