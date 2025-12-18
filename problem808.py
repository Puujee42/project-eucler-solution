def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    count = 0
    total_sum = 0
    p = 2
    
    # We loop until we find exactly 50 numbers
    while count < 50:
        if is_prime(p):
            square = p * p
            s = str(square)
            
            # Condition 1: It is not a palindrome
            if s != s[::-1]:
                rev_s = s[::-1]
                rev_square = int(rev_s)
                
                # Check if reverse is a perfect square
                root = int(rev_square**0.5)
                if root * root == rev_square:
                    # Condition 3: Its reverse is also the square of a prime
                    if is_prime(root):
                        total_sum += square
                        count += 1
                        # Optional: Print progress
                        # print(f"{count}: {square} (from {p}^2), reverse {rev_square} (from {root}^2)")
        p += 1
        
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(result)