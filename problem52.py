def solve_permuted_multiples():
    x = 1
    while True:
        # Optimization: x must start with 1. 
        # If x starts with 2 or more, 6*x will have more digits than x.
        # We can verify this with string length.
        
        str_x = str(x)
        str_6x = str(6 * x)
        
        if len(str_6x) > len(str_x):
            # If 6x has more digits, jump to the next power of 10
            # e.g., if checking 17 and 6*17=102, jump to 100
            x = 10**len(str_x)
            continue
            
        # Get the sorted digits of x as a reference
        # sorted('321') -> ['1', '2', '3']
        digits_x = sorted(str_x)
        
        # Check multipliers 2, 3, 4, 5, 6
        # We check them in order. If any fail, we stop.
        found = True
        for k in range(2, 7):
            if sorted(str(x * k)) != digits_x:
                found = False
                break
        
        if found:
            return x
        
        x += 1

if __name__ == "__main__":
    result = solve_permuted_multiples()
    print(f"The smallest positive integer is: {result}")