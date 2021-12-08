with open("day8/input.txt", 'r') as f:
    nums = [line for line in f.readlines()]
    part1 = [line.split("|")[1].strip().split() for line in nums]

# Unique numbers
n_8 = 7
n_1 = 2
n_4 = 4
n_7 = 3
digs = set([n_1, n_4, n_7, n_8])
unique_digits = {7: 8, 2: 1, 4: 4, 3: 7}
#print(part1)

count = 0
for line in part1:
    for dig in line:
        if len(dig) in unique_digits:
            count += 1
#print(count)

# Part 2
# Go for each line
true_segs = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

def decode(digs_right, true_to_false_map, false_to_true_map):
    decoded = []
    for dig in digs_right:
        decoding = []
        for c in dig:
            decoding.append(false_to_true_map[c])
        decoded_dig = ''.join(sorted(decoding))
        decoded.append(str(true_segs[decoded_dig]))
    return int(''.join(decoded))

final_nums = []
for i in range(len(nums)):
    digs_left = nums[i].split("|")[0].strip().split()
    digs_left = [''.join(sorted(dig)) for dig in digs_left]
    digs_right = nums[i].split("|")[1].strip().split()
    digs_right = [''.join(sorted(dig)) for dig in digs_right]
    digs = digs_left # + digs_right

    from collections import defaultdict
    display_map_left = {}
    display_map_right = {}
    display_map = {}
    unique_digits = defaultdict(lambda: 'X', unique_digits)
    false_to_true_map = defaultdict(lambda: 'x')
    true_to_false_map = defaultdict(lambda: 'x')

    # Create maps
    for i in range(0, len(digs)):
        digit = set(digs[i])
        display_map[i] = unique_digits[len(digit)]
        inverse_display_map = {v: k for k, v in display_map.items() if v != 'X'}

    if 1 in inverse_display_map and 7 in inverse_display_map:
        digit_1 = set(digs[inverse_display_map[1]])
        digit_7 = set(digs[inverse_display_map[7]])
        true_to_false_map['a'] = list((digit_1 ^ digit_7))[0]
        false_to_true_map[list((digit_1 ^ digit_7))[0]] = 'a'
    if 7 in inverse_display_map and 4 in inverse_display_map:
        digit_7 = set(digs[inverse_display_map[7]])
        digit_4 = set(digs[inverse_display_map[4]])
        true_to_false_map['a'] = list(digit_7 - digit_4)[0]
        false_to_true_map[list(digit_7 - digit_4)[0]] = 'a'

    # Get 9
    almost_9 = set(digs[inverse_display_map[4]] + true_to_false_map['a'])
    digs_set = [set(dig) for dig in digs]
    for i in range(len(digs_set)):
        s = digs_set[i]
        if s.intersection(almost_9) == almost_9 and len(s) != 7:
            true_to_false_map['g'] = list(s - almost_9)[0]
            false_to_true_map[list(s - almost_9)[0]] = 'g'
            display_map[i] = 9
            inverse_display_map[9] = i


    # So now we have 9 we can get true e from 8
    digit_8 = set(digs[inverse_display_map[8]])
    digit_9 = set(digs[inverse_display_map[9]])
    
    true_e = list(digit_8 - digit_9)[0]
    true_to_false_map['e'] = true_e
    false_to_true_map[true_e] = 'e'

    # Honestly do I deserve to be coding right now
    digit_6 = [dig for dig in digs_set if len(dig) == len(digit_9) and dig != digit_9 and len(dig - digit_7) > 3][0]

    true_c = list(digit_9 - digit_6)[0]
    true_to_false_map['c'] = true_c
    false_to_true_map[true_c] = 'c'

    # 5 + 1 is 9 by some mathematical axiom
    for s in digs_set:
        if s.union(digit_1) == digit_9 and len(s) < 6:
            digit_5 = s

    true_f = list(digit_1 - set(true_to_false_map['c']))[0]
    true_to_false_map['f'] = true_f
    false_to_true_map[true_f] = 'f'

    # ANOTHER FOR LOOP??!!!!
    for s in digs_set:
        if len(s - digit_1) == 3:
            digit_3 = s

    true_d = list(digit_3 - digit_7 - set(true_to_false_map['g']))[0]
    true_to_false_map['d'] = true_d
    false_to_true_map[true_d] = 'd'

    # Finally get b
    false_values_already = set(true_to_false_map.values())
    true_b = list(set('abcdefg') - false_values_already)[0]
    true_to_false_map['b'] = true_b
    false_to_true_map[true_b] = 'b'
    
    output_num = decode(digs_right, true_to_false_map, false_to_true_map)
    final_nums.append(output_num)

# This oneshot the challenge, but I believe I've lost my sanity and morals doing it
print(sum(final_nums))

# Notes from the start
# 1 and 7 can deduce what a is
# 7 and 4 can deduce what a is
# 9 is 4 and 1 or 4 and 7 plus extra thing
# 8 and 6 can deduce what c is 
# 5 and 6 can deduce what e is
# 8 and 9 can deduce what e is
# 6 and 9 can deduce what c and e are