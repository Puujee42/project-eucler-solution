def sum_square_digits(n):
    """Calculates the sum of the square of the digits of n."""
    s = 0
    while n:
        digit = n % 10
        s += digit * digit
        n //= 10
    return s

def solve():
    limit = 10000000  # Ten million
    max_chain_start = 567 # 7 * 9**2. Max SSD for numbers < 10 million.

    # chain_ends[i] will store whether i ends in 89 (True) or 1 (False).
    chain_ends = {}

    # Calculate chains for numbers up to max_chain_start
    for start_num in range(1, max_chain_start + 1):
        num = start_num
        seen = set()  # To detect loops (though we know it always goes to 1 or 89)

        while num != 1 and num != 89 and num not in seen:
            seen.add(num)
            num = sum_square_digits(num)

        chain_ends[start_num] = (num == 89)  # True if ends in 89, False if ends in 1

    # Count numbers below the limit that end in 89
    count = 0
    for i in range(1, limit):
        num = i
        while num > max_chain_start:
            num = sum_square_digits(num)

        if chain_ends[num]:
            count += 1

    return count

result = solve()
print(result)