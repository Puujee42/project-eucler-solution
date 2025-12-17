def is_palindrome(s):
    """Checks if a string is a palindrome."""
    return s == s[::-1]

def solve_double_base_palindromes():
    limit = 1000000
    total_sum = 0
    
    # We only check odd numbers because binary palindromes must end in 1 
    # (since they start with 1), which makes them odd.
    for n in range(1, limit, 2):
        # Check base 10
        if is_palindrome(str(n)):
            # Check base 2 (remove '0b' prefix)
            if is_palindrome(bin(n)[2:]):
                total_sum += n
                
    return total_sum

if __name__ == "__main__":
    result = solve_double_base_palindromes()
    print(f"The sum of all numbers less than one million which are palindromic in base 10 and base 2 is: {result}")