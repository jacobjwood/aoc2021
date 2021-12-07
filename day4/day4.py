with open("day4/input.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]
    bingo_list = []
    num_line = nums[0]
    for line in nums[1:]:
        if line == '':
            temp_list = []
        else:
            temp_list.append(line)
            if len(temp_list) == 5:
                bingo_list.append(temp_list)

bingo_list1 = [[line.split() for line in bingo_board] for bingo_board in bingo_list]

#bingo_list1 = [[int(i) for i in row] for board in bingo_list1 for row in board]

x = None
y = None

# So I can index properly
# No duplicates on a bingo card
bingo_line = ['X', 'X', 'X', 'X', 'X']
winning_boards = []
num_turns = []
final_nums_called = []

# Time-independent bingo
# So we don't mutate the original list
bingo_list2 = bingo_list1
for board in bingo_list2:
    count = 0
    for num in num_line.split(','):
        count += 1
        for row in range(len(board)):
            if num in board[row]:
                board[row][board[row].index(num)] = 'X'
        rows = board
        columns = [[row[i] for row in board] for i in range(len(rows))]
        if bingo_line in rows or bingo_line in columns:
            winning_boards.append(board)
            num_turns.append(count)
            final_nums_called.append(num)
            break

# Change min or max depending on part 1 or part 2
first_winning_board = winning_boards[num_turns.index(max(num_turns))]
final_num = final_nums_called[num_turns.index(max(num_turns))]
winning_board_nums = [int(num) for row in first_winning_board for num in row if num != 'X']
#print(first_winning_board)
#print(sum(winning_board_nums))
#print(final_num)
print(794 * 42) # part 1
print(208 * 39) # part 2