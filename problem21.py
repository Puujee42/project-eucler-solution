def sum_proper_divisors(n):
    """Calculates the sum of proper divisors of n."""
    if n <= 1:
        return 0
    total = 1
    # We only need to check up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            # Add the corresponding divisor if it's not the same (perfect square)
            if i != n // i:
                total += n // i
    return total

def solve():
    amicable_sum = 0
    limit = 10000
    
    # Iterate through all numbers under the limit
    for a in range(2, limit):
        b = sum_proper_divisors(a)
        
        # Check amicable conditions:
        # 1. b must not be equal to a (amicable numbers are pairs of distinct numbers)
        # 2. The sum of proper divisors of b must be equal to a
        if b != a and sum_proper_divisors(b) == a:
            amicable_sum += a
            
    return amicable_sum

if __name__ == "__main__":
    result = solve()
    print(f"The sum of all amicable numbers under 10,000 is: {result}")