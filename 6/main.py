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
            if grid[i][j] in ["^", "v", "<", ">"]:
                return (i, j)
    raise ValueError("No starting position found")


def get_next_position(grid, x, y):
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


def simulate(grid):
    rows, cols = len(grid), len(grid[0])
    x, y = get_starting_position(grid)
    seen_blocks = set()
    loops = False

    next_x, next_y = get_next_position(grid, x, y)
    while 0 <= next_x < rows and 0 <= next_y < cols:
        if grid[next_x][next_y] in ["X", "."]:
            grid[next_x][next_y] = grid[x][y]
            grid[x][y] = "X"
            x, y = next_x, next_y
        elif grid[next_x][next_y] == "#":
            if (next_x, next_y, grid[x][y]) in seen_blocks:
                loops = True
                break
            seen_blocks.add((next_x, next_y, grid[x][y]))
            match grid[x][y]:
                case "^":
                    grid[x][y] = ">"
                case "v":
                    grid[x][y] = "<"
                case "<":
                    grid[x][y] = "^"
                case ">":
                    grid[x][y] = "v"
        next_x, next_y = get_next_position(grid, x, y)

    visited = [
        (x, y)
        for x in range(rows)
        for y in range(cols)
        if grid[x][y] not in [".", "#"]
    ]

    return visited, loops


def part1(grid):
    visited, _ = simulate(grid)
    print("Part 1: ", len(visited))
    return visited


def part2(grid, visited):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = get_starting_position(grid)
    count = 0
    for r, c in visited:
        if (r, c) == (start_x, start_y):
            continue
        grid_copy = [row[:] for row in grid]
        grid_copy[r][c] = "#"
        _, loops = simulate(grid_copy)
        count += int(loops)

    print("Part 2: ", count)


def main():
    grid = read_input("6/input.txt")
    visited = part1([row[:] for row in grid])
    part2([row[:] for row in grid], visited)


if __name__ == "__main__":
    main()
