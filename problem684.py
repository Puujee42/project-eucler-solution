import sys

def solve():
    # Define the modulo constant
    MOD = 1_000_000_007

    # 1. Generate Fibonacci sequence up to f_90
    # f_0 = 0, f_1 = 1, f_i = f_{i-1} + f_{i-2}
    fib = [0] * 91
    fib[1] = 1
    for i in range(2, 91):
        fib[i] = fib[i-1] + fib[i-2]

    # Function to calculate S(k) using the derived formula
    def get_S_k(k):
        # We decompose k into k = 9*q + r
        q = k // 9
        r = k % 9

        # Formula: S(k) = 10^q * (6 + r(r+3)/2) - (6 + 9q + r)
        
        # Calculate term coefficient: C = 6 + r(r+3)/2
        # Since r is small (0-8), this is a small integer.
        coeff = 6 + (r * (r + 3)) // 2

        # Calculate modular exponentiation for 10^q
        # Note: q is the exponent, which can be very large. 
        # Python's pow(base, exp, mod) handles this efficiently.
        pow_10 = pow(10, q, MOD)

        # First part of the formula
        part_a = (pow_10 * coeff) % MOD

        # Second part of the formula (linear terms)
        # q is large, so we must modulo it for the addition
        part_b = (6 + 9 * (q % MOD) + r) % MOD

        # Combine parts
        ans = (part_a - part_b + MOD) % MOD
        return ans

    # 2. Compute the sum of S(f_i) for i = 2 to 90
    total_sum = 0
    for i in range(2, 91):
        val = get_S_k(fib[i])
        total_sum = (total_sum + val) % MOD

    print(f"The answer is: {total_sum}")

if __name__ == "__main__":
    solve()