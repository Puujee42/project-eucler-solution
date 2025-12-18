def solve_champernowne_constant():
    # We need digits up to the 1,000,000th index.
    # Appending to a list is more efficient than string concatenation in a loop.
    champernowne_list = []
    length = 0
    curr_int = 1
    target = 1000005  # Slightly more than 1 million
    
    while length < target:
        s = str(curr_int)
        champernowne_list.append(s)
        length += len(s)
        curr_int += 1
        
    # Join to form the full string
    # The string represents 123456789101112...
    fractional_part = "".join(champernowne_list)
    
    # Indices to check (1-based index n corresponds to string index n-1)
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    product = 1
    
    for i in indices:
        digit_char = fractional_part[i - 1]
        digit_val = int(digit_char)
        product *= digit_val
        
    return product

if __name__ == "__main__":
    result = solve_champernowne_constant()
    print(f"The value of the expression is: {result}")