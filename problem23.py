def solve_non_abundant_sums():
    # The problem states that all integers greater than 28123 can be written as the sum of two abundant numbers.
    LIMIT = 28123
    
    # Step 1: Calculate sum of proper divisors for all numbers up to LIMIT using a sieve approach.
    # We initialize with 0. 
    # Logic: i divides j if j is a multiple of i.
    div_sums = [0] * (LIMIT + 1)
    for i in range(1, LIMIT // 2 + 1):
        for j in range(i * 2, LIMIT + 1, i):
            div_sums[j] += i
            
    # Step 2: Identify abundant numbers
    # An abundant number n satisfies div_sums[n] > n
    abundants = [n for n in range(12, LIMIT + 1) if div_sums[n] > n]
    
    # Step 3: Mark numbers that can be written as the sum of two abundant numbers
    can_be_written = [False] * (LIMIT + 1)
    
    # We iterate through the list of abundant numbers to mark their sums
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            abundant_sum = abundants[i] + abundants[j]
            if abundant_sum > LIMIT:
                break
            can_be_written[abundant_sum] = True
            
    # Step 4: Sum all numbers that cannot be written as the sum of two abundant numbers
    total_sum = 0
    for x in range(1, LIMIT + 1):
        if not can_be_written[x]:
            total_sum += x
            
    return total_sum

if __name__ == "__main__":
    result = solve_non_abundant_sums()
    print(f"The sum of all positive integers which cannot be written as the sum of two abundant numbers is: {result}")