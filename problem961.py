def solve():
    # The problem asks for W(10^18).
    # Based on the analysis, the formula for W(10^(2m)) is (10^(2m) - (-8)^m) // 6.
    
    exponent = 18
    m = exponent // 2  # m = 9
    
    # Calculate terms
    term1 = 10**exponent
    term2 = (-8)**m
    
    # Apply formula
    # W(10^18) = (10^18 - (-8)^9) / 6
    # Since m is odd, (-8)^9 is negative, so it becomes addition: (10^18 + 8^9) / 6
    result = (term1 - term2) // 6
    
    return result

if __name__ == "__main__":
    print(solve())