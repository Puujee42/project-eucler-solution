def solve_triangle_words():
    filename = "words.txt"
    
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        return "Error: 'words.txt' not found. Please ensure it is in the same directory."

    # Parse the file: remove quotes and split by comma
    words = data.replace('"', '').split(',')
    
    # Generate a set of triangle numbers
    # The longest word is unlikely to exceed a score of 1000 (approx 38 'Z's)
    # t_n = n(n+1)/2
    triangle_numbers = set()
    n = 1
    while True:
        t = (n * (n + 1)) // 2
        if t > 1000:  # Safe upper limit
            break
        triangle_numbers.add(t)
        n += 1

    count = 0
    for word in words:
        # Calculate word value: A=1, B=2, ... (ASCII - 64)
        word_value = sum(ord(char) - 64 for char in word)
        
        # Check if the value is a triangle number
        if word_value in triangle_numbers:
            count += 1
            
    return count

if __name__ == "__main__":
    result = solve_triangle_words()
    print(f"Number of triangle words: {result}")