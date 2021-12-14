with open("day14/input.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]
    precursor = nums[0]
    insertions = [num.split('->') for num in nums[2:]]
    insertions = [(num[0].strip(), num[1].strip()) for num in insertions]

print(precursor)

# Part 1 is not going to work for part 2

count = 0
while count < 10:
    precursor = [[p for p in precursor[i:i+2]] for i in range(len(precursor))]
    insertions = dict(insertions)
    for p in precursor:
        if len(p) == 2:
            pre = ''.join(p)
            p[1:1] = insertions[pre]
        p = ''.join(p)

    pre_unjoined = [p[:2] if len(p) > 1 else p[0] for p in precursor]
    pre_unjoined = [i for p in pre_unjoined for i in p]
    precursor = ''.join(pre_unjoined)
    count += 1

from collections import Counter

counts = Counter(pre_unjoined)
common = counts.most_common()
print(common[0][1] - common[-1][1])

# Part 2 is going to require some thought
precursor = nums[0]
pairs = [precursor[i:i+2] for i in range(len(precursor))]

from collections import defaultdict

pair_count = defaultdict(int)

for p in pairs:
    if len(p) > 1:
        pair_count[p] += 1

count=0
while count < 40:
    pair_count1 = pair_count.copy()
    for k, v in pair_count.items():
        next_pair1 = f"{k[0]}{insertions[k]}"
        next_pair2 = f"{insertions[k]}{k[1]}"
        pair_count1[next_pair1] += v 
        pair_count1[next_pair2] += v
        pair_count1[k] -= v
    pair_count = pair_count1
    count += 1

letter_count = defaultdict(int)

for k, v in pair_count.items():
    letter_count[k[1]] += v
    letter_count[k[0]] += v

# Account for S, V at the end
letter_count["V"] += 1
letter_count["S"] += 1
letter_count = {k: int(v/2) for k, v in letter_count.items()}

maxi = 0
mini = 100000000000000000000
max_k = None
min_k = None
for k, v in letter_count.items():
    maxi = max([v, maxi])
    mini = min([v, mini])
    if maxi == v:
        max_k = k
    if mini == v:
        min_k = k

print(letter_count[max_k] - letter_count[min_k])
    