import requests
from collections import Counter

if __name__ == "__main__":
    left_list, right_list = [], []

    # Read from input.txt instead of fetching
    with open('1/input.txt', 'r') as file:
        for line in file:
            left_num, right_num = map(int, line.split())
            left_list.append(left_num)
            right_list.append(right_num)

    # Part 1
    print(sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list))))

    # Part 2
    right_nums_count = Counter(right_list)
    print(sum(right_nums_count[num] * num for num in left_list))
