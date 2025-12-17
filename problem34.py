def solve_digit_factorials():
    # Precompute factorials for digits 0-9
    factorials = [1] * 10
    for i in range(2, 10):
        factorials[i] = factorials[i - 1] * i

    # Define the upper limit based on the analysis (7 * 9!)
    limit = 2540160
    total_sum = 0
    
    # Iterate from 3 to the limit
    for n in range(3, limit):
        current_n = n
        fact_sum = 0
        
        # Calculate sum of factorials of digits
        # We can extract digits using modulo arithmetic for speed, 
        # or convert to string (slightly slower but easier to read).
        # Given the limit, string conversion is fast enough in Python.
        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            fact_sum += factorials[digit]
            temp_n //= 10
            # Optimization: If partial sum exceeds n, we can stop early
            if fact_sum > n:
                break
        
        if fact_sum == n:
            total_sum += n

    return total_sum

if __name__ == "__main__":
    result = solve_digit_factorials()
    print(f"The sum of all numbers equal to the sum of the factorial of their digits is: {result}")