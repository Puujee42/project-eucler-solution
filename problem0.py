def calculate(limit):
    if(limit % 2 != 0 ):
        odd_number = limit + 1
        odd_number = odd_number // 2
    else:
        odd_number = limit // 2
    quadratic = odd_number * (odd_number + 1) * (2 * odd_number + 1) // 6 
    single = odd_number * (odd_number + 1) // 2
    summer = 4 * quadratic - 4 * single  + odd_number
    print(summer)
calculate(895000)