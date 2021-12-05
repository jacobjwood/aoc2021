with open("day5/input.txt", 'r') as f:
    nums = [[l.strip().split(',') for l in line.split('->')] for line in f.readlines()]
    # Cheap implementation of xor using nequal to get horizontal/vertical
    nums1 = [points for points in nums if (points[0][0] == points[1][0]) != (points[0][1] == points[1][1])]
    # Diagonals with 45 degrees have deltaX = deltaY
    nums2 = [points for points in nums if (abs(int(points[0][0]) - int(points[1][0])) == abs(int(points[0][1]) - int(points[1][1])))]

# Need a function that gets points of a line
def get_points1(nums_list):
    points = []
    for line_coords in nums_list:
        x1 = int(line_coords[0][0])
        x2 = int(line_coords[1][0])
        y1 = int(line_coords[0][1])
        y2 = int(line_coords[1][1])
        if x1 == x2:
            points += [(x1, i) for i in range(min(y1, y2), max(y1, y2)+1)]
        if y1 == y2:
            points += [(i, y1) for i in range(min(x1, x2), max(x1, x2)+1)]
    return points
    
# Part 1
points = get_points1(nums1)

intersections = set([])
temps = set([])
for p in points:
    if p in temps and p not in intersections:
        intersections.add(p)
    if p not in temps:
        temps.add(p)

print(len(intersections))

# Part 2

def get_points2(list_nums):
    points = []
    for line_coords in list_nums:
        x1 = int(line_coords[0][0])
        x2 = int(line_coords[1][0])
        y1 = int(line_coords[0][1])
        y2 = int(line_coords[1][1])
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        if (x1 < x2) and (y1 < y2):
            points += [(i, j) for i, j in zip(range(x_min, x_max+1), range(y_min, y_max+1))]
        elif (x1 < x2) and (y1 > y2):
            points += [(i, j) for i, j in zip(range(x_min, x_max+1), range(y_max, y_min-1, -1))]
        elif (x1 > x2) and (y1 < y2):
            points += [(i, j) for i, j in zip(range(x_max, x_min-1, -1), range(y_min, y_max+1))]
        elif (x1 > x2) and (y1 > y2):
            points += [(i, j) for i, j in zip(range(x_max, x_min-1, -1), range(y_max, y_min-1, -1))]
    return points

points2 = get_points2(nums2)
points1 = get_points1(nums1)
points = points1 + points2

intersections2 = set([])
temps2 = set([])
for p in points:
    if p in temps2 and p not in intersections2:
        intersections2.add(p)
    if p not in temps2:
        temps2.add(p)

print(len(intersections2))


    
