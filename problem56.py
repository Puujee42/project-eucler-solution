def solve_max_digital_sum():
    max_sum = 0
    
    # Iterate a and b from 1 to 99 (since a, b < 100)
    for a in range(1, 100):
        for b in range(1, 100):
            # Calculate power
            power_val = a ** b
            
            # Calculate sum of digits
            # Convert number to string, iterate chars, convert back to int, and sum
            current_sum = sum(int(digit) for digit in str(power_val))
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

if __name__ == "__main__":
    result = solve_max_digital_sum()
    print(f"The maximum digital sum is: {result}")