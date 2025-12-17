import time

def collatz(limit):
    """
    Finds the starting number under 'limit' with the longest Collatz chain.
    The core logic with memoization (caching) is efficient and correct.
    """
    # Cache to store the lengths of chains we've already computed.
    # The +1 is to allow indexing up to 'limit'.
    chain_lengths = [0] * (limit + 1)
    
    max_length = 0
    starting_number_for_max = 0

    # We only need to check numbers up to the limit.
    for i in range(1, limit):
        count = 0
        val = i
        while val > 1:
            if val < limit and chain_lengths[int(val)] > 0:
                count += chain_lengths[int(val)]
                break
            
            if val % 2 == 0:
                val = val / 2
            else:
                val = 3 * val + 1
            count += 1
        
        total_chain_length = count + 1
        chain_lengths[i] = total_chain_length

        if total_chain_length > max_length:
            max_length = total_chain_length
            starting_number_for_max = i
            
    return starting_number_for_max

# --- Main execution ---
start_time = time.time()

# FIX 1: The problem specifies a limit of one million.
LIMIT = 1000000 

# FIX 2: Call the function only ONCE and store the result.
number_with_longest_chain = collatz(LIMIT)

end_time = time.time()

# FIX 3: Print the stored result, not by calling the function again.
print(f"The starting number under {LIMIT} with the longest chain is: {number_with_longest_chain}")
print(f"Calculation took: {end_time - start_time:.4f} seconds")