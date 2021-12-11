with open("day10/input.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]

points_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
part2_points_map = {')': 1, ']': 2, '}': 3, '>': 4}
open_to_close_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
opening = set(['(', '[', '{', '<'])
closing = set([')', ']', '}', '>'])

# Part 1 and Part 2 prep
total = 0
non_corrupt = []
for line in nums:
    corrupt = False
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        if char in closing and char != open_to_close_map[stack.pop()]:
            total += points_map[char]
            corrupt = True

    if corrupt:
        continue

    non_corrupt.append(line)

print(total)

# Part 2
line_totals = []   
for line in non_corrupt:
    total = 0
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            stack.pop()
    
    # Remaining stack
    while len(stack) != 0:
        char = stack.pop()
        total *= 5 
        total += part2_points_map[open_to_close_map[char]]
        #print(char, total)
    line_totals.append(total)

print(sorted(line_totals)[len(line_totals) // 2])



