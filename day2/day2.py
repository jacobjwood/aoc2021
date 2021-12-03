with open("day2/input.txt", 'r') as f:
    nums = [tuple(line.split()) for line in f.readlines()]
    nums = [(i[0], int(i[1])) for i in nums]
    set_nums = set(nums)
    depth = 0
    horiz = 0
    aim = 0
    for t in nums:
        if t[0] == 'up':
            #depth -= t[1]
            aim -= t[1]
        if t[0] == 'down':
            #depth += t[1]
            aim += t[1]
        if t[0] == 'forward':
            horiz += t[1]
            depth += aim*t[1]
    print(depth * horiz)