with open("day7/input.txt", 'r') as f:
    nums = [line for line in f.readlines()]
    positions = nums[0].split(',')
    positions = [int(pos) for pos in positions]

cost = 0
min_pos = min(positions)
max_pos = max(positions)

def get_meet(part2=False):

    def series_sum(x, part2):
        if part2:
            return int(x * (x + 1) / 2)
        else:
            return x
    
    costs = []

    for same_pos in range(min_pos, max_pos+1):
        moves = [series_sum(abs(same_pos - pos), part2) for pos in positions]
        costs.append(sum(moves))
    
    print(min(costs))

get_meet()
get_meet(part2=True)