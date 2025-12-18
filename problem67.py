def solve_max_path_sum():
    try:
        # Read the file content
        with open('triangle.txt', 'r') as f:
            data = f.read().strip().split('\n')
        
        # Parse the data into a list of lists of integers
        triangle = [[int(num) for num in line.split()] for line in data]

        # Iterate from the second-to-last row up to the top
        # range(start, stop, step) -> start at len-2, go down to 0
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update the current element with the max of its two children
                triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

        # The top element now contains the maximum path sum
        return triangle[0][0]

    except FileNotFoundError:
        return "File 'triangle.txt' not found."

if __name__ == "__main__":
    print(solve_max_path_sum())