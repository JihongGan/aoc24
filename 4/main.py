def read_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),   # right
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 0),  # up
        (-1, 1)   # up-right
    ]

    def check_word(row, col, dx, dy):
        word = "XMAS"
        for i in range(len(word)):
            new_row = row + i * dx
            new_col = col + i * dy
            if (new_row < 0 or new_row >= rows or 
                new_col < 0 or new_col >= cols or 
                grid[new_row][new_col] != word[i]):
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_word(row, col, dx, dy):
                    count += 1

    return count

def count_xmas2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_cross_pattern(i, j):
        if i + 2 >= rows or j + 2 >= cols:
            return False
            
        patterns = [
            # M.M    M.S    S.S    S.M
            # .A.    .A.    .A.    .A.
            # S.S    M.S    M.M    S.M
            
            lambda: (grid[i][j] == 'M' and
                    grid[i][j+2] == 'M' and
                    grid[i+1][j+1] == 'A' and
                    grid[i+2][j] == 'S' and
                    grid[i+2][j+2] == 'S'),
            
            lambda: (grid[i][j] == 'M' and
                    grid[i][j+2] == 'S' and
                    grid[i+1][j+1] == 'A' and
                    grid[i+2][j] == 'M' and
                    grid[i+2][j+2] == 'S'),
            
            lambda: (grid[i][j] == 'S' and
                    grid[i][j+2] == 'S' and
                    grid[i+1][j+1] == 'A' and
                    grid[i+2][j] == 'M' and
                    grid[i+2][j+2] == 'M'),
            
            lambda: (grid[i][j] == 'S' and
                    grid[i][j+2] == 'M' and
                    grid[i+1][j+1] == 'A' and
                    grid[i+2][j] == 'S' and
                    grid[i+2][j+2] == 'M')
        ]
        
        return any(pattern() for pattern in patterns)
    
    for i in range(rows):
        for j in range(cols):
            if check_cross_pattern(i, j):
                count += 1
                
    return count

def main():
    input = read_input("4/input.txt")
    print("Part 1:", count_xmas(input))
    print("Part 2:", count_xmas2(input))

if __name__ == "__main__":
    main()
