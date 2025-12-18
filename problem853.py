import random

# --- Mathematical Helpers ---

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

def fib_pair(n, mod):
    """
    Computes (F_n, F_{n+1}) % mod using Fast Doubling.
    """
    if n == 0:
        return (0, 1)
    
    # Recursively find (F_k, F_{k+1}) for k = n // 2
    a, b = fib_pair(n >> 1, mod)
    
    # Formulas:
    # F_2k = F_k * (2*F_{k+1} - F_k)
    # F_{2k+1} = F_{k+1}^2 + F_k^2
    c = a * (2 * b - a)
    d = a * a + b * b
    
    if n & 1:
        return (d % mod, (c + d) % mod)
    else:
        return (c % mod, d % mod)

def get_pisano_period_prime_power(p, k, limit=120):
    """
    Finds the period of p^k. Since we know the period must divide 120,
    we only check divisors of 120.
    """
    mod = p ** k
    # Divisors of 120
    divs = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
    
    for d in divs:
        # Check if period is d: F_d == 0 and F_{d+1} == 1
        f0, f1 = fib_pair(d, mod)
        if f0 == 0 and f1 == 1:
            return d
    return 0 # Should not happen based on problem logic

# --- Factorization (Pollard's Rho) ---

def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def is_prime_miller_rabin(n, k=10):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def pollard_rho(n):
    if n == 1: return 1
    if n % 2 == 0: return 2
    
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n: # failure, retry
            return pollard_rho(n)
            
    return d

def factorize(n):
    factors = {}
    if n == 1: return factors
    
    queue = [n]
    while queue:
        temp = queue.pop()
        if temp == 1: continue
        if is_prime_miller_rabin(temp):
            factors[temp] = factors.get(temp, 0) + 1
            continue
        
        d = pollard_rho(temp)
        queue.append(d)
        queue.append(temp // d)
    return factors

# --- Main Solution ---

def solve():
    LIMIT = 1_000_000_000
    TARGET_PERIOD = 120

    # 1. Calculate F_120 and F_121
    # We do exact integer arithmetic
    F_120, F_121 = fib_pair(120, 10**100) # Large enough mod to get exact value

    # 2. Find G = gcd(F_120, F_121 - 1)
    # n must divide G to have pi(n) | 120
    G = gcd(F_120, F_121 - 1)
    
    # 3. Factorize G
    factors_map = factorize(G)
    
    # 4. Prepare options for DFS
    # options[i] = list of tuples (prime_power_value, period)
    # We include p^0 = 1 (period 1) in every list to allow skipping a prime factor
    prime_options = []
    
    for p, max_e in factors_map.items():
        opts = []
        curr = 1
        
        # p^0
        opts.append((1, 1))
        
        # p^1 to p^max_e
        for _ in range(max_e):
            curr *= p
            if curr >= LIMIT: break
            
            per = get_pisano_period_prime_power(p, 1) # Period of prime power
            # Optimization: pi(p^k) = p^(k-1) * pi(p) usually, 
            # but we calculate explicitly to be safe and use helper
            # Actually helper takes (p, k) but we passed p. 
            # Let's fix loop to use exact power.
            
            # Recalculate exact period for this specific power q = curr
            # We can treat curr as p^k. 
            # Note: get_pisano_period_prime_power logic checks divisors of 120.
            # If period doesn't divide 120, it returns 0 (though by logic it must).
            
            # Calculating period of `curr` directly:
            per = get_pisano_period_prime_power(curr, 1) # treat curr as base with exp 1 logic-wise
            
            if per > 0:
                opts.append((curr, per))
        
        prime_options.append(opts)
    
    # 5. DFS to find sums
    total_sum = 0
    
    # Stack for DFS: (index_in_prime_options, current_number_value, current_lcm_of_periods)
    stack = [(0, 1, 1)]
    
    while stack:
        idx, curr_val, curr_lcm = stack.pop()
        
        if idx == len(prime_options):
            if curr_lcm == TARGET_PERIOD:
                total_sum += curr_val
            continue
        
        # Try all powers of the current prime
        for val, per in prime_options[idx]:
            next_val = curr_val * val
            
            if next_val < LIMIT:
                # Optimization: if LCM already exceeds 120 or doesn't divide 120?
                # No, LCM grows. It must divide 120.
                next_lcm = lcm(curr_lcm, per)
                
                # If next_lcm > 120 or 120 % next_lcm != 0, this branch is invalid for exact 120
                if 120 % next_lcm == 0:
                    stack.append((idx + 1, next_val, next_lcm))

    print(f"Sum of values: {total_sum}")

if __name__ == "__main__":
    solve()