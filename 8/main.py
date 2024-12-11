from collections import defaultdict


def read_input(file_path):
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            # Strip any whitespace/newlines and convert line to list of chars
            row = list(line.strip())
            grid.append(row)
    return grid


def main():
    grid = read_input("8/input.txt")
    rows, cols = len(grid), len(grid[0])

    antennas = defaultdict(list)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append((i, j))

    def get_antinodes1():
        antinodes = set()
        for antenna, positions in antennas.items():
            for i, (x1, y1) in enumerate(positions):
                for x2, y2 in positions[i + 1 :]:
                    for x, y in [
                        (x1 + x1 - x2, y1 + y1 - y2),
                        (x2 + x2 - x1, y2 + y2 - y1),
                    ]:
                        if 0 <= x < rows and 0 <= y < cols:
                            antinodes.add((x, y))
        return antinodes

    antinodes = get_antinodes1()
    print("Part 1:", len(antinodes))

    def get_line(x1, y1, x2, y2):
        line = []

        x, y = x1, y1
        dx, dy = x1 - x2, y1 - y2
        while 0 <= x < rows and 0 <= y < cols:
            line.append((x, y))
            x += dx
            y += dy

        x, y = x2, y2
        dx, dy = x2 - x1, y2 - y1
        while 0 <= x < rows and 0 <= y < cols:
            line.append((x, y))
            x += dx
            y += dy

        return line

    def get_antinodes2():
        antinodes = set()
        for antenna, positions in antennas.items():
            for i, (x1, y1) in enumerate(positions):
                for x2, y2 in positions[i + 1 :]:
                    for x, y in get_line(x1, y1, x2, y2):
                        if 0 <= x < rows and 0 <= y < cols:
                            antinodes.add((x, y))
        return antinodes

    antinodes = get_antinodes2()
    print("Part 2:", len(antinodes))


if __name__ == "__main__":
    main()
