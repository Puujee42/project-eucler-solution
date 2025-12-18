import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Given constants
    N = 10**14
    M = 1234567891
    
    n_half = N // 2
    
    # --- Calculate Term 1 ---
    # S1 = 2^(N-1) * Sum_{k=1 to n/2} k
    # Sum_{k=1 to H} k = H(H+1)/2
    
    # Calculate sum of k modulo M
    # Note: M is odd, so inverse of 2 exists
    sum_k = (n_half % M) * ((n_half + 1) % M) % M * pow(2, -1, M) % M
    
    term1 = pow(2, N - 1, M) * sum_k % M
    
    # --- Calculate Term 2 ---
    # S2 = Sum_{k=1 to n/2} k * 2^(N - floor(N/k))
    term2 = 0
    K = int(N**0.5)
    
    # Part A: k from 1 to K (direct summation)
    # Here floor(N/k) changes rapidly, so we compute each term.
    # We perform O(sqrt(N)) modular exponentiations.
    for k in range(1, K + 1):
        if k > n_half: break
        v = N // k
        # Term: k * 2^(N-v)
        val = (k * pow(2, N - v, M)) % M
        term2 = (term2 + val) % M
        
    # Part B: k from K+1 to n_half (group by value of v = floor(N/k))
    # v ranges from floor(N/(K+1)) down to 2
    v_max = N // (K + 1)
    
    # Precompute power for the starting v
    # As v decreases by 1, the exponent (N - v) increases by 1, so we multiply by 2.
    current_pow = pow(2, N - v_max, M)
    
    for v in range(v_max, 1, -1):
        # Find range of k such that floor(N/k) == v
        # Condition: v <= N/k < v+1  =>  k <= N/v  and  k > N/(v+1)
        r = N // v
        l = (N // (v + 1)) + 1
        
        # We restrict the range to [K+1, n_half]
        start = max(l, K + 1)
        end = min(r, n_half)
        
        if start <= end:
            count = end - start + 1
            # Sum of k in [start, end] = (start + end) * count / 2
            sum_range = (start + end) * count // 2
            sum_range %= M
            
            # Add to total
            add_val = (sum_range * current_pow) % M
            term2 = (term2 + add_val) % M
            
        # Update power for next iteration (v -> v-1)
        current_pow = (current_pow * 2) % M
        
    # Final Result
    ans = (term1 - term2 + M) % M
    print(ans)

if __name__ == "__main__":
    solve()