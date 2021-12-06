with open("day6/input.txt", 'r') as f:
    nums = [line.strip().split(',') for line in f.readlines()][0]
    nums = [int(num) for num in nums]

def get_fish_after_n_days(nums, days=80):
    n_fish = {}
    for i in range(9):
        n_fish[i] = len([num for num in nums if num == i])

    for i in range(days):
        # Can probably do this with less hardcoding
        n_fish0_temp = n_fish[1]
        n_fish[1] = n_fish[2]
        n_fish[2] = n_fish[3]
        n_fish[3] = n_fish[4]
        n_fish[4] = n_fish[5]
        n_fish[5] = n_fish[6]
        n_fish[6] = n_fish[7] + n_fish[0]
        n_fish[7] = n_fish[8]
        n_fish[8] = n_fish[0]
        n_fish[0] = n_fish0_temp
    
    return n_fish

def get_total(n_fish):
    total = 0
    for i, j in n_fish.items():
        total += j
    return total

# Pt 1
print(get_total(get_fish_after_n_days(nums, days=80)))

# Pt 2
print(get_total(get_fish_after_n_days(nums, days=256)))








        
            
