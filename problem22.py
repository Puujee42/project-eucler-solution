def solve_names_scores():
    filename = "names.txt"
    
    try:
        # Step 1: Read the file data
        with open(filename, 'r') as f:
            # .strip() removes any accidental whitespace/newlines at start or end
            data = f.read().strip()
    except FileNotFoundError:
        return "Error: 'names.txt' not found. Please ensure it is in the same directory."

    # Step 2: Parse the file
    # Remove quotes and split by comma
    names = data.replace('"', '').split(',')
    
    # Step 3: Sort the list alphabetically
    names.sort()
    
    total_score = 0
    
    # Step 4: Calculate scores
    for rank, name in enumerate(names, 1):
        # Safety check to skip empty strings if any exist
        if name:
            # Calculate value: A=1 (65-64), B=2 (66-64), etc.
            name_value = sum(ord(char) - 64 for char in name)
            
            # Multiply by the position (rank)
            total_score += name_value * rank
        
    return total_score

if __name__ == "__main__":
    result = solve_names_scores()
    print(f"The total of all the name scores in the file is: {result}")