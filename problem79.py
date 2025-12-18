def solve_passcode():
    filename = "keylog.txt"
    
    # Step 1: Get the data locally
    try:
        with open(filename, 'r') as f:
            # .splitlines() handles various newline formats (\n, \r\n) better
            data = f.read().strip().splitlines()
    except FileNotFoundError:
        return "Error: 'keylog.txt' not found. Please ensure it is in the same directory."

    # Step 2: Build the graph of constraints
    # 'prereqs' maps a digit to a set of digits that MUST precede it.
    prereqs = {}
    unique_chars = set()

    for attempt in data:
        attempt = attempt.strip()
        if not attempt: 
            continue
        
        # Ensure the line has at least 3 characters
        if len(attempt) < 3:
            continue
            
        digits = list(attempt) # e.g., ['3', '1', '9']
        unique_chars.update(digits)
        
        # Ensure keys exist in dictionary for all seen digits
        for d in digits:
            if d not in prereqs:
                prereqs[d] = set()
        
        # Add constraints: 
        # 1st digit comes before 2nd -> 2nd has 1st as prerequisite
        prereqs[digits[1]].add(digits[0])
        # 2nd digit comes before 3rd -> 3rd has 2nd as prerequisite
        prereqs[digits[2]].add(digits[1])

    # Step 3: Topological Sort
    passcode = ""
    
    # We loop until we have used all unique characters
    while len(passcode) < len(unique_chars):
        next_digit = None
        
        # We look for a character that has no remaining prerequisites.
        # We sort the list to ensure deterministic behavior.
        for char in sorted(list(unique_chars)):
            if char not in passcode: # If we haven't placed this digit yet
                if len(prereqs[char]) == 0:
                    next_digit = char
                    break
        
        if next_digit:
            passcode += next_digit
            
            # Remove this digit from other digits' prerequisites
            # (Since we've "solved" this digit, it no longer blocks others)
            for key in prereqs:
                if next_digit in prereqs[key]:
                    prereqs[key].remove(next_digit)
        else:
            return "Error: Cycle detected or logic failure."

    return passcode

if __name__ == "__main__":
    result = solve_passcode()
    print(f"The shortest secret passcode is: {result}")