def calculate(limit):
    limit -= 1
    threes = limit // 3 
    fives = limit // 5
    fifteens = limit // 15
    threes_sum = threes * (threes + 1) // 2 
    fives_sum = fives * (fives + 1) // 2
    fifteens_sum = fifteens * (fifteens + 1) // 2
    sumer = threes_sum * 3 + fives_sum * 5   - fifteens_sum * 15
    print(sumer)
calculate(1000)