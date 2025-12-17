def solve_pandigital_products():
    pandigital_products = set()
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # Case 1: 1-digit x 4-digit = 4-digit
    for m in range(2, 10):  # M is 1-digit (excluding 1)
        # N must be 4 digits. Start at 1234 (smallest 4 distinct digits).
        # We stop when product > 9999.
        for n in range(1234, 10000 // m + 1):
            p = m * n
            s = str(m) + str(n) + str(p)
            if len(s) == 9 and set(s) == digits:
                pandigital_products.add(p)

    # Case 2: 2-digit x 3-digit = 4-digit
    for m in range(12, 100):  # M is 2-digit
        # N must be 3 digits. Start at 123.
        # We stop when product > 9999.
        for n in range(123, 10000 // m + 1):
            p = m * n
            s = str(m) + str(n) + str(p)
            if len(s) == 9 and set(s) == digits:
                pandigital_products.add(p)

    return sum(pandigital_products)

if __name__ == "__main__":
    result = solve_pandigital_products()
    print(f"The sum of all pandigital products is: {result}")