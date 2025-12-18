def is_pandigital(s):
    """Checks if string s is a 1-9 pandigital."""
    return len(s) == 9 and set(s) == set('123456789')

def solve_largest_pandigital_product():
    largest_pandigital = 0
    
    # M cannot have 5 digits or more, because M*1 (5) + M*2 (5 or 6) > 9 digits.
    # So we iterate M from 1 to 9999.
    # To find the largest, we can just iterate and update the max, 
    # or iterate backwards from 9999.
    
    for m in range(1, 10000):
        concatenated = ""
        n = 1
        while len(concatenated) < 9:
            concatenated += str(m * n)
            n += 1
            
        # Check if valid length and pandigital
        if len(concatenated) == 9 and is_pandigital(concatenated):
            num_val = int(concatenated)
            if num_val > largest_pandigital:
                largest_pandigital = num_val
                
    return largest_pandigital

if __name__ == "__main__":
    result = solve_largest_pandigital_product()
    print(f"The largest 1 to 9 pandigital concatenated product is: {result}")