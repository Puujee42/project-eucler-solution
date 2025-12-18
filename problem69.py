def solve():
    limit = 1000000
    result = 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # Enough primes to exceed 1,000,000
    
    i = 0
    while i < len(primes):
        if result * primes[i] > limit:
            break
        result *= primes[i]
        i += 1
        
    print(result)

if __name__ == "__main__":
    solve()