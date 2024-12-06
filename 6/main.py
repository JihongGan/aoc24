from collections import deque


def read_input(file_path):
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def get_starting_position(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in ["#", "."]:
                return (i, j)


def main():
    grid = read_input("6/input.txt")
    rows = len(grid)
    cols = len(grid[0])
    num_positions = 1
    x, y = get_starting_position(grid)

    def get_next_position(x, y):
        match grid[x][y]:
            case "^":
                x -= 1
            case "v":
                x += 1
            case "<":
                y -= 1
            case ">":
                y += 1
        return x, y

    next_x, next_y = get_next_position(x, y)
    while 0 <= next_x < rows and 0 <= next_y < cols:

        if grid[next_x][next_y] in ["X", "."]:
            if grid[next_x][next_y] == ".":
                num_positions += 1
            grid[next_x][next_y] = grid[x][y]
            grid[x][y] = "X"
            x, y = next_x, next_y
        elif grid[next_x][next_y] == "#":
            match grid[x][y]:
                case "^":
                    grid[x][y] = ">"
                case "v":
                    grid[x][y] = "<"
                case "<":
                    grid[x][y] = "^"
                case ">":
                    grid[x][y] = "v"
        next_x, next_y = get_next_position(x, y)

    print("Part 1: ", num_positions)


if __name__ == "__main__":
    main()
