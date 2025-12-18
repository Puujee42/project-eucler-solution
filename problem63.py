def solve():
    count = 0
    # The base 'k' must be less than 10.
    # If k >= 10, then k^n >= 10^n, which has at least n+1 digits.
    for k in range(1, 10):
        n = 1
        while True:
            # Calculate the power
            value = k ** n
            
            # Get the number of digits
            num_digits = len(str(value))
            
            # Check if the condition is met
            if num_digits == n:
                count += 1
            elif num_digits < n:
                # If digits < n, k^n has fallen behind 10^(n-1).
                # Since k < 10, it will never catch up.
                break
            
            # Note: num_digits > n is impossible for k < 10
            
            n += 1
            
    return count

if __name__ == "__main__":
    result = solve()
    print(f"The number of such integers is: {result}")