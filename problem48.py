def solve_last_ten_digits():
    limit = 1000
    modulo = 10**10
    total_sum = 0
    
    for n in range(1, limit + 1):
        # Calculate n^n % modulo
        term = pow(n, n, modulo)
        total_sum = (total_sum + term) % modulo
        
    return total_sum

if __name__ == "__main__":
    result = solve_last_ten_digits()
    # Format as a string with 10 digits, padding with zeros if necessary
    print(f"The last ten digits of the series are: {result:010d}")