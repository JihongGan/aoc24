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

def combinable2(nums, target):
    results = [nums[0]]
    i = 1
    while i < len(nums):
        new_results = []
        for n in results:
            new_results.extend([n * nums[i], n + nums[i], int(str(n) + str(nums[i]))])
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
    s1, s2 = 0, 0
    for target, nums in records:
        if combinable(nums, target):
            s1 += target
        if combinable2(nums, target):
            s2 += target
    print("Part 1: ", s1)
    print("Part 2: ", s2)

if __name__ == "__main__":
    main()
