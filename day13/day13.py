with open("day13/jacks_file.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]
    split_index = nums.index('')
    print(nums)
    coords, instructions = nums[:split_index], nums[split_index+1:]
    coords = [coord.split(',') for coord in coords]
    coords = [(int(i[0]), int(i[1])) for i in coords]


split_instructions = [instruction.split()[2].split('=') for instruction in instructions]
max_dim_x = max([2 * int(i[1]) for i in split_instructions if i[0]=="x"])
max_dim_y = max([2 * int(i[1]) for i in split_instructions if i[0]=="y"])
print(max_dim_x, max_dim_y)
print(instructions)

test = [
['#.##.|#..#.'],
['#...#|.....'],
['.....|#...#'],
['#...#|.....'],
['.#.#.|#.###'],
['.....|.....'],
['.....|.....']
]

test = [[char for t1 in t for char in t1] for t in test]

set_coords = set(coords)

# Create grid
paper = []
for i in range(0, max_dim_y+1):
    row = []
    for j in range(0, max_dim_x+1):
        if (j, i) in set_coords:
            row.append("#")
        else:
            row.append(".")
    paper.append(row)


def part2(paper=paper, instructions=instructions):

    instructions = [instruction.split()[2].split('=') for instruction in instructions]
    prev_instruction = None

    for i in instructions:
        # Take transpose if folding in x, or if previous fold was x (retranspose)
        if (i[0] == 'x' and prev_instruction != 'x') or (i[0] == 'y' and prev_instruction == 'x'):
            paper = [list(col) for col in zip(*paper)]
        fold = int(i[1])
        up = paper[:fold]
        down = paper[fold+1:]
        inverted_down = down.copy()
        inverted_down.reverse()

        for p in range(len(up)):
            for q in range(len(up[p])):
                if inverted_down[p][q] == "#":
                    up[p][q] = inverted_down[p][q]

        paper = up

        # Not the most efficient, just needed to check if it was folding properly
        dot_count = 0
        for n in paper:
            for o in n:
                if o == "#":
                    dot_count += 1
        
        print(dot_count)
        prev_instruction = i[0]
    if prev_instruction == 'x':
        print("watch_out")
    return paper

        
# Part 1 is first printed line (671)
final_paper = part2()
for i in final_paper:
    print(i)
#PCPHARKL
