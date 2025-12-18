def solve_consecutive_prime_factors():
    # Define a limit for the search. 
    # Based on the growth from the 3-consecutive case (around 644), 
    # 200,000 is a safe initial upper bound guess.
    limit = 200000
    
    # distinct_factors[i] will store the number of distinct prime factors of i
    distinct_factors = [0] * limit
    
    # Step 1: Populate the factors count using a sieve approach
    for i in range(2, limit):
        # If distinct_factors[i] is 0, i is prime
        if distinct_factors[i] == 0:
            # Increment the count for all multiples of this prime
            for j in range(i, limit, i):
                distinct_factors[j] += 1
                
    # Step 2: Find 4 consecutive numbers with 4 distinct prime factors
    # We stop at limit - 4 to avoid index out of bounds
    for i in range(2, limit - 4):
        if (distinct_factors[i] == 4 and 
            distinct_factors[i+1] == 4 and 
            distinct_factors[i+2] == 4 and 
            distinct_factors[i+3] == 4):
            return i

if __name__ == "__main__":
    result = solve_consecutive_prime_factors()
    print(f"The first of these numbers is: {result}")