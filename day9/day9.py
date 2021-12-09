with open("day9/input.txt", 'r') as f:
    nums = [[int(l) for l in line.strip()] for line in f.readlines()]

low_points = []
low_points_locs = []

def padding(lists_to_pad):
    for row in lists_to_pad:
        row.append(100)
        row.insert(0, 100)
    top_bottom_padding = [100] * len(lists_to_pad[0])
    lists_to_pad.append(top_bottom_padding)
    lists_to_pad.insert(0, top_bottom_padding)

padding(nums)

for r in range(len(nums)):
    for c in range(len([col for col in zip(*nums)])):
        if nums[r][c] == 100:
            continue
        else:
            point_of_interest = nums[r][c]
            convolving_cross = [nums[r-1][c], nums[r+1][c], nums[r][c+1], nums[r][c-1]]
            if point_of_interest < min(convolving_cross):
                low_points.append(point_of_interest)
                low_points_locs.append((r, c))

danger = [p+1 for p in low_points]
print(sum(danger))

# Basins
def expand_out(point):
    r = point[0]
    c = point[1]
    points_below_nine = [(r, c)]

    def recursive_mess(points_below_nine, previous_len=0):
        for point in points_below_nine:
            r = point[0]
            c = point[1]

            down = nums[r-1][c]
            down_point = (r-1, c)
            up = nums[r+1][c]
            up_point = (r+1, c)
            right = nums[r][c+1]
            right_point = (r, c+1)
            left = nums[r][c-1]
            left_point = (r, c-1)

            points_below_nine += [dir_point for dir_point, direction in zip([up_point, down_point, left_point, right_point], [up, down, left, right]) if direction < 9]
            points_below_nine = list(set(points_below_nine))

        if previous_len == len(points_below_nine):
            return points_below_nine
        else:
            previous_len = len(set(points_below_nine))
            points_below_nine = list(set(points_below_nine))
            return recursive_mess(points_below_nine, previous_len)

    points_below_nine = recursive_mess(points_below_nine)
    return len(set(points_below_nine))

basin_sizes = []
for point in low_points_locs:
    basin_sizes.append(expand_out(point))
print(sorted(basin_sizes)[-3:])
print(94*96*102)



        

    

        
