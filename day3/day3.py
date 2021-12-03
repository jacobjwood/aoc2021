with open("day3/input.txt", 'r') as f:
    nums1 = [line.strip() for line in f.readlines()]
    nums = [[n for n in num] for num in nums1]

digit_counts = []
for digit in range(12):
    count = 0
    for num in nums:
        count += int(num[digit])
    digit_counts.append(count)

gam_digits = [str(1) if i > 500 else str(0) for i in digit_counts]
eps_digits = [str(0) if i > 500 else str(1) for i in digit_counts]

gam = ''.join(gam_digits)
eps = ''.join(eps_digits)

gam_bin = int(gam, 2)
eps_bin = int(eps, 2)

print("part 1: ", gam_bin * eps_bin)

# Part 2 - very inelegant but works
# Take nums_list, list of binary nums as strings
# Strings allow taking each digit separately
# i is the index of the string we want to access and inverse determines whether we take CO2 or not
def get_it(nums_list, i=0, co2=False):
    # Base case
    if len(nums_list) == 1:
        return int(str(nums_list[0]), 2)

    # Otherwise run this monstrosity
    count_0 = sum([int(num[i]) + 1 for num in nums_list if num[i] == '0'])
    count_1 = sum([int(num[i]) for num in nums_list])
    if count_0 > count_1:
        if not co2:
            nums_list = [num for num in nums_list if num[i] == '0']
        else:
            nums_list = [num for num in nums_list if num[i] == '1']
    elif count_1 > count_0:
        if not co2:
            nums_list = [num for num in nums_list if num[i] == '1']
        else:
            nums_list = [num for num in nums_list if num[i] == '0']
    else:
        if not co2:
            nums_list = [num for num in nums_list if num[i] == '1']
        else: 
            nums_list = [num for num in nums_list if num[i] == '0']
    i += 1
    return get_it(nums_list, i=i, co2=co2)

print("part 2: ", get_it(nums1, co2=True) * get_it(nums1, co2=False))





