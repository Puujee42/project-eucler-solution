def solve():
    # Initialize with the first expansion: 3/2
    numerator = 3
    denominator = 2
    
    count = 0
    
    # Iterate for the first 1000 expansions
    for _ in range(1000):
        # Check if the number of digits in numerator exceeds denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
            
        # Calculate the next numerator and denominator using the recurrence relation
        # Next Numerator = Current Numerator + 2 * Current Denominator
        # Next Denominator = Current Numerator + Current Denominator
        # We use tuple unpacking to update both simultaneously safely
        numerator, denominator = numerator + 2 * denominator, numerator + denominator
        
    return count

if __name__ == "__main__":
    result = solve()
    print(f"Number of fractions with more digits in numerator: {result}")