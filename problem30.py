def solve_fifth_powers():
    # Precompute fifth powers for digits 0-9
    powers = [i**5 for i in range(10)]
    
    # Upper bound explanation: 6 * 9^5 = 354,294.
    # 7 * 9^5 = 413,343, but min 7-digit number is 1,000,000.
    # So we can stop checking safely around 355,000.
    limit = 355000
    total_sum = 0
    
    # Iterate from 2 to limit
    for n in range(2, limit):
        # Calculate sum of 5th powers of digits
        # Converting to string is fast enough for this range
        digit_sum = sum(powers[int(d)] for d in str(n))
        
        if digit_sum == n:
            total_sum += n
            
    return total_sum

if __name__ == "__main__":
    result = solve_fifth_powers()
    print(f"The sum of all numbers that can be written as the sum of fifth powers of their digits is: {result}")