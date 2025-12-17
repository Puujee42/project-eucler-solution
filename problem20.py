def count_combinations():
    target = 200
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    ways = [0] * (target + 1)
    
    ways[0] = 1
    
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
            
    return ways[target]

result = count_combinations()
print(f"The number of different ways to make £2 is: {result}")