def solve_spiral_diagonals():
    limit = 1001
    total_sum = 1  # Start with the center number
    
    # Iterate through each layer side length (3, 5, 7, ..., 1001)
    for L in range(3, limit + 1, 2):
        # Apply the formula for the sum of the four corners: 4*L^2 - 6*(L-1)
        layer_corner_sum = 4 * (L**2) - 6 * (L - 1)
        total_sum += layer_corner_sum
        
    return total_sum

if __name__ == "__main__":
    result = solve_spiral_diagonals()
    print(f"The sum of the numbers on the diagonals in a 1001x1001 spiral is: {result}")