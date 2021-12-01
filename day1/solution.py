with open("day1/input.txt", "r+") as f:
  depths = [int(line) for line in f.readlines()]
  count = 0
  for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
      count += 1
  print(count)
  
  count_slide = 0
  for i in range(1, len(depths) - len(depths)%3):
    if depths[i] + depths[i+1] + depths[i+2] > depths[i-1] + depths[i] + depths[i+1]:
      count_slide += 1
  print(count_slide)

# One liners
# Part one
counts1 = sum([1 if depths[i] > depths[i-1] else 0 for i in range(1, len(depths))])
print(counts1)
# Part two
counts2 = sum([1 if sum(depths[i-3:i]) < sum(depths[i-2:i+1]) else 0 for i in range(3, len(depths))])
print(counts2)
