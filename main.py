import sys

DEBUG = False

def parse_file(filename):
    with open(filename, "r") as f:
        # The first line represents the size of the matrix
        line = f.readline()
        line_split = line.split(" ")
        rows = int(line_split[0])
        cols = int(line_split[1])
        # Initialize the y,x matrix with the first line
        data = []
        while True:
            # Loop until we have read the last line
            line = f.readline().rstrip()
            if line == "":
                break
            line_split = line.split(" ")
            data.append(line_split)
        # Return a tuple
        return (rows, cols, data)


def dfs(data, y_orig, x_orig, cols, rows, visited):
    stack = [(y_orig, x_orig)]
    total = 0
    while len(stack):
        (y, x) = stack.pop(0)
        if visited[y][x]:
            continue
        total += 1
        visited[y][x] = True
        # Top
        if y > 0 and not visited[y-1][x] and data[y-1][x] == data[y][x]:
            stack.append((y-1, x))
        # Left
        if x > 0 and not visited[y][x-1] and data[y][x-1] == data[y][x]:
            stack.append((y, x-1))
        # Right
        if x < cols -1 and not visited[y][x+1] and data[y][x+1] == data[y][x]:
            stack.append((y, x+1))
        # Bottom
        if y < rows -1 and not visited[y+1][x] and data[y+1][x] == data[y][x]:
            stack.append((y+1, x))
    return total


def solve(file_data):
    (rows, cols, data) = file_data
    longest_sequence = 0
    visited = [[False for x in range(cols)] for y in range(rows)]
    for y in range(0, rows):
        for x in range(0, cols):
            if visited[y][x]:
                continue
            # Start a DFS from each cell and keep track of the longest sequence
            longest_sequence = max(longest_sequence, dfs(data, y, x, cols, rows, visited))
    return longest_sequence

files = sys.argv[1:]
if DEBUG:
    print("Reading files", files)

files_data = []
for f in files:
    files_data.append(parse_file(f))

if DEBUG:
    print("Parsed data", files_data)

for f in files_data:
    print(solve(f))