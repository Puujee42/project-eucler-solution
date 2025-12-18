import sys
from decimal import Decimal, getcontext, ROUND_HALF_UP

def solve():
    # Set precision high enough to handle the accumulation of terms and the required output
    getcontext().prec = 150
    
    # Initialization
    # We are given that the sequence starts with a_1 = 2.
    # Therefore, theta starts with "2."
    theta_str = "2."
    
    # We need to express b_n as a linear function of theta: b_n = M * theta - C
    # Base case:
    # b_1 = theta.  (M=1, C=0)
    # a_1 = floor(b_1) = 2.
    #
    # Calculate coefficients for b_2:
    # b_2 = a_1 * (b_1 - a_1 + 1)
    # b_2 = 2 * (theta - 2 + 1) 
    # b_2 = 2 * theta - 2
    
    M = Decimal(2)
    C = Decimal(2)
    
    # Target: 24 decimal places.
    # We generate a few extra digits to ensure correct rounding.
    required_digits = 24
    target_length = 2 + required_digits + 5  # "2." + digits + safety buffer
    
    while len(theta_str) < target_length:
        # Parse the current known string of theta as a Decimal
        # This acts as a lower bound for the true value of theta
        theta_curr = Decimal(theta_str)
        
        # Calculate the current value of b_n based on this estimate
        b_val = M * theta_curr - C
        
        # Determine the next term in the sequence
        # Since b_n grows based on theta, and theta is built from these integers,
        # the floor of this lower-bound estimate is the correct integer.
        a_n = int(b_val)
        
        # Append the new integer to the decimal string
        theta_str += str(a_n)
        
        # Update coefficients for b_{n+1} using the recurrence relation:
        # b_{n+1} = a_n * (b_n - a_n + 1)
        # Substitute b_n = M*theta - C:
        # b_{n+1} = a_n * (M*theta - C - a_n + 1)
        # b_{n+1} = (a_n * M) * theta - a_n * (C + a_n - 1)
        
        a_n_dec = Decimal(a_n)
        
        # Update M and C
        M = a_n_dec * M
        C = a_n_dec * (C + a_n_dec - 1)
        
    # Round the result to 24 decimal places
    final_theta = Decimal(theta_str)
    quantizer = Decimal("1." + "0" * required_digits)
    result = final_theta.quantize(quantizer, rounding=ROUND_HALF_UP)
    
    print(f"Theta rounded to {required_digits} places:")
    print(result)

if __name__ == "__main__":
    solve()