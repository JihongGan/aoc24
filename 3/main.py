import re

def part_1():
    # Read input file
    with open('3/input.txt', 'r') as file:
        text = file.read()

    # Find all multiplication expressions using regex
    # Pattern matches mul(X,Y) where X and Y are 1-3 digits
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, text)

    # Calculate sum of all products
    total = 0
    for match in matches:
        x = int(match.group(1))  # First captured number
        y = int(match.group(2))  # Second captured number
        total += x * y

    print("Part 1: ", total)

def part_2():
    with open('3/input.txt', 'r') as file:
        text = file.read()

    # Find all control and multiplication expressions
    # We'll process them in order of appearance
    control_pattern = r'(?:do|don\'t)\(\)'
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Combine patterns and use named groups to distinguish them
    combined_pattern = f'(?P<control>{control_pattern})|(?P<mul>{mul_pattern})'
    
    enabled = True  # Start with multiplications enabled
    total = 0
    
    for match in re.finditer(combined_pattern, text):
        if match.group('control'):
            # Update enabled state based on control instruction
            enabled = match.group('control') == 'do()'
        elif match.group('mul') and enabled:
            # Process multiplication only if enabled
            mul_match = re.match(mul_pattern, match.group('mul'))  # Re-match to get numbered groups
            x = int(mul_match.group(1))
            y = int(mul_match.group(2))
            total += x * y

    print("Part 2:", total)

if __name__ == "__main__":
    part_1()
    part_2()
