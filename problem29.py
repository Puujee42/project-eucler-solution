def count_distinct_powers():
    # Use a set to store distinct terms
    distinct_terms = set()
    
    # Iterate through all values of a and b from 2 to 100
    for a in range(2, 101):
        for b in range(2, 101):
            term = a ** b
            distinct_terms.add(term)
            
    # Return the size of the set
    return len(distinct_terms)

if __name__ == "__main__":
    result = count_distinct_powers()
    print(f"The number of distinct terms is: {result}")