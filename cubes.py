def calculate(limit):
    collect = {}
    for i in range(1, limit):
        for j in range(i, limit):
            sum = i ** 3 + j ** 3
            if sum in collect:
                pair1 = collect[sum]
                pair2 = (i, j)
                if pair1[0] != pair2[0] and pair1[1] != pair2[1]:
                    print(f"{pair1[0]}^3 + {pair1[1]}^3 = {pair2[0]}^3 + {pair2[1]}^3 = {sum}")
            else:
                collect[sum] = (i , j)
calculate(1000)