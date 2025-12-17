import math

def solve_curious_fractions():
    fractions = []
    
    for d in range(11, 100):
        for n in range(10, d):
            # Trivial example check: ending in 0
            if n % 10 == 0 and d % 10 == 0:
                continue
            
            # Convert to strings to check digits
            str_n = str(n)
            str_d = str(d)
            
            # Find common digits
            common_digits = set(str_n) & set(str_d)
            
            for digit in common_digits:
                # '0' cancellation is considered trivial (e.g. 30/50)
                if digit == '0':
                    continue
                
                # Remove the common digit. 
                # We need to handle cases carefully (e.g. one instance vs two).
                # The problem implies simple cancellation.
                # Construct new numerator/denominator by removing one instance of the digit.
                
                # Note: This logic assumes we remove specific matching instances.
                # However, for 2-digit numbers, usually it's the 'diagonal' cancellation 
                # (units of num cancel tens of den).
                
                # Remove digit from n
                idx_n = str_n.find(digit)
                new_n_str = str_n[:idx_n] + str_n[idx_n+1:]
                val_n = int(new_n_str)
                
                # Remove digit from d
                idx_d = str_d.find(digit)
                new_d_str = str_d[:idx_d] + str_d[idx_d+1:]
                val_d = int(new_d_str)
                
                # Avoid division by zero
                if val_d == 0:
                    continue
                
                # Check if values are equal
                # n/d == val_n/val_d  =>  n * val_d == d * val_n
                if n * val_d == d * val_n:
                    fractions.append((n, d))

    # The problem states there are exactly 4 such fractions.
    # Let's verify and calculate the product.
    
    prod_n = 1
    prod_d = 1
    
    for n, d in fractions:
        prod_n *= n
        prod_d *= d
        
    # Simplify the fraction
    gcd = math.gcd(prod_n, prod_d)
    
    return prod_d // gcd

if __name__ == "__main__":
    result = solve_curious_fractions()
    print(f"The denominator of the product is: {result}")