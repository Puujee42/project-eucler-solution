import itertools

def solve():
    total_sum = 0
    
    # We can optimize by checking the specific divisibility conditions starting from the "hardest" ones
    # d8 d9 d10 is divisible by 17
    # d7 d8 d9 is divisible by 13
    # ...
    
    # Let's generate valid suffixes and extend backwards
    
    # Step 1: d8 d9 d10 divisible by 17
    # Digits must be distinct
    suffixes_17 = []
    for d8 in range(10):
        for d9 in range(10):
            if d9 == d8: continue
            for d10 in range(10):
                if d10 == d8 or d10 == d9: continue
                num = 100 * d8 + 10 * d9 + d10
                if num % 17 == 0:
                    suffixes_17.append([d8, d9, d10])
                    
    # Step 2: d7 d8 d9 divisible by 13
    suffixes_13 = []
    for s in suffixes_17:
        d8, d9, d10 = s
        for d7 in range(10):
            if d7 in s: continue
            num = 100 * d7 + 10 * d8 + d9
            if num % 13 == 0:
                suffixes_13.append([d7] + s)

    # Step 3: d6 d7 d8 divisible by 11
    suffixes_11 = []
    for s in suffixes_13:
        d7, d8, d9, d10 = s
        for d6 in range(10):
            if d6 in s: continue
            num = 100 * d6 + 10 * d7 + d8
            if num % 11 == 0:
                suffixes_11.append([d6] + s)
                
    # Step 4: d5 d6 d7 divisible by 7
    suffixes_7 = []
    for s in suffixes_11:
        d6, d7, d8, d9, d10 = s
        for d5 in range(10):
            if d5 in s: continue
            num = 100 * d5 + 10 * d6 + d7
            if num % 7 == 0:
                suffixes_7.append([d5] + s)

    # Step 5: d4 d5 d6 divisible by 5
    # Since d6 must be 0 or 5, this filters heavily
    suffixes_5 = []
    for s in suffixes_7:
        d5, d6, d7, d8, d9, d10 = s
        # The number d4 d5 d6 implies d6 is 0 or 5. This is already determined by d6 in the suffix.
        # We just need to find d4 that is distinct.
        if d6 != 0 and d6 != 5:
            continue
            
        for d4 in range(10):
            if d4 in s: continue
            # d4 d5 d6 is div by 5 is always true if d6 is 0 or 5
            suffixes_5.append([d4] + s)

    # Step 6: d3 d4 d5 divisible by 3
    suffixes_3 = []
    for s in suffixes_5:
        d4, d5, d6, d7, d8, d9, d10 = s
        for d3 in range(10):
            if d3 in s: continue
            num = d3 + d4 + d5 # Divisibility by 3 depends on sum
            if num % 3 == 0:
                suffixes_3.append([d3] + s)
                
    # Step 7: d2 d3 d4 divisible by 2
    suffixes_2 = []
    for s in suffixes_3:
        d3, d4, d5, d6, d7, d8, d9, d10 = s
        for d2 in range(10):
            if d2 in s: continue
            # d2 d3 d4 div by 2 means d4 is even. This is determined by d4.
            # We check if d4 is even.
            if d4 % 2 == 0:
                suffixes_2.append([d2] + s)

    # Step 8: Add d1
    final_numbers = []
    for s in suffixes_2:
        d2, d3, d4, d5, d6, d7, d8, d9, d10 = s
        for d1 in range(10):
            if d1 in s: continue
            # d1 cannot be 0 for a 10-digit number usually, 
            # though problem says "0 to 9 pandigital", typically implies d1 != 0 
            # or treat as string? "The number, 1406357289..." implies standard number.
            if d1 == 0: continue 
            
            # Construct the full number
            full_digits = [d1] + s
            num_str = "".join(map(str, full_digits))
            final_numbers.append(int(num_str))
            
    return sum(final_numbers)

if __name__ == "__main__":
    result = solve()
    print(f"The sum of all 0 to 9 pandigital numbers with the property is: {result}")