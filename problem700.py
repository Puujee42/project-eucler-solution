def solve_eulercoins():
    A = 1504170715041707
    M = 4503599627370517
    
    # The first Eulercoin is A (assuming A < M and A > 0)
    p = A
    # The initial gap from M is M - A
    g = M - A
    
    current_sum = p
    
    while p > 0 and g > 0:
        if g > p:
            # Update the 'negative' gap
            g %= p
        else:
            # p >= g
            # We find new Eulercoins: p-g, p-2g, ...
            q = p // g
            
            # Sum of arithmetic progression:
            # Sum = (p-g) + (p-2g) + ... + (p-qg)
            #     = q*p - g * (1 + 2 + ... + q)
            #     = q*p - g * (q * (q + 1) // 2)
            
            term_sum = q * p - g * (q * (q + 1) // 2)
            current_sum += term_sum
            
            p %= g
            
    return current_sum

if __name__ == "__main__":
    print(solve_eulercoins())