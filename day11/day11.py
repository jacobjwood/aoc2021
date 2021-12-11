with open("day11/input.txt", 'r') as f:
    nums = [[int(num) for num in line.strip()] for line in f.readlines()]

# Like day 9, pad the nums to make things easier with list indexing
# I could do range(min()) and range(max()) but at the time I thought this was easier
def pad_nums(nums):
    for line in nums:
        line.insert(0, -1)
        line.append(-1)
    nums.insert(0, [-1] * len(nums[0]))
    nums.append([-1] * len(nums[0]))
    return nums


def get_neighbours_and_oct_map(nums):

    neighbours_map = {}
    oct_map = {}

    for l in range(1, len(nums)-1):

        line = nums[l]

        for n in range(1, len(line)-1):
            
            # octopus
            num = line[n]
            octopus = (l, n)
            oct_map[octopus] = num

            # neighbourhood
            neighbourhood = [(l+m, n+o) for m in range(-1, 2, 1) for o in range(-1, 2, 1) if ((nums[l+m][n+o] != -1) and ((l+m, n+o) != (l, n)))]
            neighbours_map[octopus] = neighbourhood

    return neighbours_map, oct_map


def increment(oct_map):

    for k, v in oct_map.items():
        oct_map[k] += 1

    return oct_map


def find_flashes(oct_map):

    flashes = []

    for k, v in oct_map.items():

        if v > 9:
            flashes.append(k)

    return flashes


def flash(oct, oct_map, neighbours_map):

    neighbours = neighbours_map[oct]

    for n in neighbours:

        if oct_map[n] != 0:
            oct_map[n] += 1

    oct_map[oct] = 0

    return oct_map
    

def flash_pass(oct_map, neighbours_map, flash_count, flashes=None):

    if flashes is None:
        flashes = find_flashes(oct_map)

    if len(flashes) == 0:
        return oct_map, flash_count
    else:

        for oct in flashes:
            oct_map = flash(oct, oct_map, neighbours_map)
            flash_count += 1

        flashes = find_flashes(oct_map)

        return flash_pass(oct_map, neighbours_map, flash_count, flashes)


nums = pad_nums(nums)

neighbours_map, oct_map = get_neighbours_and_oct_map(nums)

counter = 0
flash_count = 0

while True:
    counter += 1
    flash_count_prev = flash_count
    oct_map = increment(oct_map)
    oct_map, flash_count = flash_pass(oct_map, neighbours_map, flash_count)

    if counter == 100:
        part1 = flash_count

    if flash_count - flash_count_prev == 100:
        part2 = counter
        break
    
print(part1)
print(part2)
