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

# hashing maybe
def hash_board(board_list):
    board_maps = []
    for board in board_list:
        board_dict = {}
        for row in range(len(board)):
            for col in range(row):
                num = board[row][col]
                pos_string = f"{row}{col}"
                board_dict[num] = pos_string
        board_maps.append(board_dict)
    return board_maps

def play_game(board_list, board_maps, nums_called):
    board_list1 = board_list
    board_maps1 = board_maps
    for num in nums_called:
        for board, board_map in zip(board_list1, board_maps1):
            if num in board_map:
                i = int(board_map[num][0])
                j = int(board_map[num][1])
                board[i][j] = 'X'
            rows = board
            cols = [col for col in zip(*board)]
            print(rows)
            print(cols)


                


play_game(bingo_list1, hash_board(bingo_list1), num_line)
    
    

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