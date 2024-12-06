from collections import defaultdict
from functools import cmp_to_key


def read_input(file_path):
    before_set = defaultdict(set)
    sequences = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                a, b = line.split("|")
                before_set[b].add(a)
            elif "," in line:
                sequences.append(line.split(","))
    return before_set, sequences


def main():
    before_set, sequences = read_input("5/input.txt")
    mid_sum_right = 0
    mid_sum_wrong = 0

    def comparator(x, y):
        if x in before_set[y]:
            return -1
        elif y in before_set[x]:
            return 1
        else:
            return 0

    for sequence in sequences:
        after = set()
        is_right_order = True
        for item in reversed(sequence):
            if before_set[item] & after:
                is_right_order = False
                break
            after.add(item)
        if is_right_order:
            mid_sum_right += int(sequence[len(sequence) // 2])
        else:
            mid_sum_wrong += int(
                sorted(sequence, key=cmp_to_key(comparator))[
                    len(sequence) // 2
                ]
            )

    print("Part 1: ", mid_sum_right)
    print("Part 2: ", mid_sum_wrong)


if __name__ == "__main__":
    main()
