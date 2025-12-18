def solve_consecutive_prime_sum():
    limit = 1000000
    
    # Step 1: Sieve of Eratosthenes to identify primes up to limit
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    # Step 2: Create cumulative sums of primes
    # We only need enough primes such that their sum exceeds the limit
    prime_sums = [0]
    current_sum = 0
    for p in primes:
        current_sum += p
        if current_sum >= limit:
            break
        prime_sums.append(current_sum)
        
    # The number of available consecutive sums is len(prime_sums) - 1
    # This corresponds to the length of the longest chain starting at 2.
    max_length = len(prime_sums) - 1
    
    # Step 3: Check lengths in descending order
    # length represents the number of primes in the sequence
    for length in range(max_length, 0, -1):
        # Check all "windows" of this length
        # i is the starting index of the sequence of primes
        for i in range(len(prime_sums) - length):
            # Sum of primes from index i to i + length - 1
            # Using cumulative array: sum = S[i+length] - S[i]
            total_sum = prime_sums[i + length] - prime_sums[i]
            
            # Optimization: If total_sum exceeds limit, consecutive windows 
            # starting later will also exceed limit (since primes are positive increasing)
            if total_sum >= limit:
                break
            
            if is_prime[total_sum]:
                return total_sum, length

if __name__ == "__main__":
    result_prime, length = solve_consecutive_prime_sum()
    print(f"The prime below one million that can be written as the sum of the most consecutive primes is: {result_prime}")
    print(f"Number of consecutive primes: {length}")