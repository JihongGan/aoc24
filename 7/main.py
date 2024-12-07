def combinable(nums, target):
    results = [nums[0]]
    i = 1
    while i < len(nums):
        new_results = []
        for n in results:
            new_results.extend([n * nums[i], n + nums[i]])
        results = new_results
        i += 1
    return target in results

def read_input(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            target_str, nums_str = line.strip().split(': ')
            target = int(target_str)
            nums = [int(x) for x in nums_str.split()]
            records.append((target, nums))
    return records

def main():
    records = read_input("7/input.txt")
    s = 0
    for target, nums in records:
        if combinable(nums, target):
            s += target
    print("Part 1: ", s)

if __name__ == "__main__":
    main()
