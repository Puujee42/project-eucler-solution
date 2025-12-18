def solve():
    """
    Finds the unique integer x whose square has the form 1_2_3_4_5_6_7_8_9_0.
    """
    # y^2 corresponds to the pattern 1_2_3_4_5_6_7_8_9 (17 digits)
    # Define the search range for y based on the min and max possible values of y^2
    min_sq_val = 10203040506070809
    max_sq_val = 19293949596979899
    
    start_y = int(min_sq_val**0.5)
    end_y = int(max_sq_val**0.5)
    
    # Iterate through the range
    for y in range(start_y, end_y + 1):
        # Optimization 1: y^2 ends in 9, so y must end in 3 or 7
        if y % 10 not in (3, 7):
            continue
            
        # Optimization 2: The hundreds digit of y^2 must be 8
        # The pattern ends in ...8_9. Index 14 is '8' (hundreds place).
        # We check this mathematically to avoid slow string conversion.
        if (y * y // 100) % 10 != 8:
            continue
            
        # Convert square to string to check the full pattern
        s = str(y * y)
        
        # Check specific positions to fail fast
        # Indices: 0 2 4 6 8 10 12 14 16
        # Values:  1 2 3 4 5  6  7  8  9
        if s[0] != '1' or s[8] != '5' or s[16] != '9':
            continue
            
        # Verify the entire pattern
        valid = True
        for i in range(9):
            # s[0] should be '1', s[2] should be '2', ..., s[16] should be '9'
            if s[2 * i] != str(i + 1):
                valid = False
                break
        
        if valid:
            # We found y, so x = 10 * y
            return y * 10

if __name__ == "__main__":
    result = solve()
    print(f"The unique integer is: {result}")
    print(f"Verification: {result}² = {result**2}")