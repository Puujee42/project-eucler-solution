import math
import sys

def solve():
    # Configuration
    L_prefix = 123
    target_n = 678910
    
    # Calculate logarithmic bounds
    # We want 1.23 <= fractional_part(10^(j*log10(2))) < 1.24
    theta = math.log10(2)
    lower_bound = math.log10(L_prefix / 100.0)      # log10(1.23)
    upper_bound = math.log10((L_prefix + 1) / 100.0) # log10(1.24)
    
    # Phase 1: Determine the pattern of gaps between solutions.
    # The 'Three Gap Theorem' states there are at most 3 distinct distances 
    # between consecutive points in such a sequence.
    hits = []
    j = 1
    
    # Find the first 100 hits to establish the pattern
    # We estimate the gap to be around 1 / (upper - lower) ~= 284.
    # Checking up to 30,000 is extremely fast.
    while len(hits) < 100:
        # Calculate fractional part of j * theta
        val = (j * theta) % 1.0
        
        if lower_bound <= val < upper_bound:
            hits.append(j)
        j += 1
        
    # Extract unique gaps (differences between consecutive solutions)
    gaps = sorted(list(set(hits[i] - hits[i-1] for i in range(1, len(hits)))))
    
    # Phase 2: Fast-forward to the target
    # Start from the last known hit
    count = len(hits)
    current_j = hits[-1]
    
    while count < target_n:
        found = False
        # Try adding known gaps to find the next valid j
        for gap in gaps:
            next_j = current_j + gap
            val = (next_j * theta) % 1.0
            
            if lower_bound <= val < upper_bound:
                current_j = next_j
                count += 1
                found = True
                break
        
        # Fallback for robustness (should not be triggered with correct gaps)
        if not found:
            curr = current_j + 1
            while True:
                val = (curr * theta) % 1.0
                if lower_bound <= val < upper_bound:
                    gaps.append(curr - current_j)
                    gaps.sort()
                    current_j = curr
                    count += 1
                    break
                curr += 1
                
    return current_j

if __name__ == "__main__":
    result = solve()
    print(f"p(123, 678910) = {result}")