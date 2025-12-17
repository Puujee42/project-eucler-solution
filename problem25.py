def solve_fibonacci_digits():
    # Initialize the first two terms
    # F_1 = 1, F_2 = 1
    a = 1
    b = 1
    index = 2
    
    # Iterate until the number of digits in 'b' is 1000
    # len(str(b)) converts the number to a string and counts characters
    while len(str(b)) < 1000:
        # Calculate next term
        a, b = b, a + b
        index += 1
        
    return index

if __name__ == "__main__":
    result = solve_fibonacci_digits()
    print(f"The index of the first Fibonacci number to contain 1000 digits is: {result}")