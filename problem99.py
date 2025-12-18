import math

def solve():
    max_value = 0
    best_line_number = 0
    current_line_number = 0

    try:
        # Open the file containing the base/exponent pairs
        # Ensure 'base_exp.txt' is in the same directory as this script
        with open('base_exp.txt', 'r') as file:
            for line in file:
                current_line_number += 1
                
                # Parse the line (format: base,exponent)
                parts = line.strip().split(',')
                if len(parts) < 2:
                    continue
                
                base = int(parts[0])
                exponent = int(parts[1])
                
                # Calculate the magnitude using logarithms
                # value = exponent * log(base)
                magnitude = exponent * math.log(base)
                
                # Check if this is the largest value we've seen so far
                if magnitude > max_value:
                    max_value = magnitude
                    best_line_number = current_line_number

        print(f"The line number with the greatest numerical value is: {best_line_number}")

    except FileNotFoundError:
        print("Error: The file 'base_exp.txt' was not found.")

if __name__ == "__main__":
    solve()