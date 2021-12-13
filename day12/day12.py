with open("day12/input.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]
    nums = [tuple(num.split('-')) for num in nums]

def make_map(cave_tuples):

    cave_map = {}

    for tup in cave_tuples:

        cave1 = tup[0]
        cave2 = tup[1]

        if cave1 not in cave_map:
            cave_map[cave1] = [cave2]
        else: 
            cave_map[cave1].append(cave2)

        if cave2 not in cave_map:
            cave_map[cave2] = [cave1]
        else:
            cave_map[cave2].append(cave1)

    return cave_map


cave_map = make_map(nums)


def solver(G, part2=False):

    paths = []

    def dfs(G, v, visited=[], visited_twice=False, path=[], part2=part2):

        path.append(v)

        if v == "end":
            paths.append(path)
            return

        if v.islower():
            visited.append(v)

        for w in G[v]:

            if w == "start":
                continue

            if (w not in visited):
                dfs(G, w, visited.copy(), visited_twice=visited_twice, path=path.copy(), part2=part2)
            elif (w in visited and not visited_twice and part2):
                dfs(G, w, visited, visited_twice=True, path=path.copy())


    dfs(cave_map, "start", part2=part2)
    return paths


paths1 = solver(cave_map, part2=False)
paths2 = solver(cave_map, part2=True)

print(len(paths1))
print(len(paths2))