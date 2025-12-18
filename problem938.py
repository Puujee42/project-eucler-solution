def solve():
    R = 24690
    B = 12345
    r_target = R // 2
    b_target = B
    
    # q[b] will store the value of q(r, b)
    # Initialize for r=0: q(0, b) = 0, but q(r, 0) = 1
    # We maintain the array for b = 1 to B
    # q[0] is conceptually 1
    
    q = [0.0] * (b_target + 1)
    q[0] = 1.0
    
    for r in range(1, r_target + 1):
        num_r = 2 * r - 1
        current_q = 1.0 # This is q(r, 0)
        
        for b in range(1, b_target + 1):
            num_b = 2 * b
            denom = num_r + num_b
            
            # Recurrence:
            # q(r, b) = ( (2r-1)*q(r-1, b) + (2b)*q(r, b-1) ) / denom
            # q[b] currently holds q(r-1, b)
            # current_q holds q(r, b-1)
            
            val = (num_r * q[b] + num_b * current_q) / denom
            q[b] = val
            current_q = val
            
    return 1.0 - q[b_target]

print(f"{solve():.10f}")