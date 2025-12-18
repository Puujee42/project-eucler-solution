def is_palindrome(n):
    """Checks if a number is a palindrome."""
    s = str(n)
    return s == s[::-1]

def solve_lychrel_numbers():
    lychrel_count = 0
    limit = 10000
    
    for n in range(1, limit):
        current_val = n
        is_lychrel = True
        
        # Try to find a palindrome within 50 iterations
        for _ in range(50):
            # Reverse and add
            rev_val = int(str(current_val)[::-1])
            current_val += rev_val
            
            # Check if the result is a palindrome
            if is_palindrome(current_val):
                is_lychrel = False
                break
        
        if is_lychrel:
            lychrel_count += 1
            
    return lychrel_count

if __name__ == "__main__":
    result = solve_lychrel_numbers()
    print(f"The number of Lychrel numbers below 10,000 is: {result}")