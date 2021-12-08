import sys

orig_stdout = sys.stdout
input = open('input.txt', 'r')
output = open('out2.txt', 'w')
sys.stdout = output

inputs = input.readlines()

number_string = inputs[0].strip()
numbers = number_string.split(',')

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def boardNumbers(board_array):
    board = []
    for row in board_array:
        for num in row:
            if num not in board:
                board.append(num)
    return board

boards = []
for idx in range(2, len(inputs), 6):
    rows = []
    for row_idx in range(idx, idx + 5):
        row_string = inputs[row_idx].strip()
        row = row_string.split()
        rows.append(row)

    columns =[]
    for column_idx in range(5):
        column = []
        for row in rows:
            column.append(row[column_idx])
        columns.append(column)    

    board = rows + columns
    boards.append(board) 

def checkWin(called, boards, won_boards):
    winning_boards = []
    for index, board in enumerate(boards, start=0):
        if index not in won_boards:
            for row in board:
                inter = intersection(called, row)
                if len(inter) == 5:
                    num = called[-1]
                    win = {'board': index, 'length': len(called), 'number': num}
                    winning_boards.append(win)
    return winning_boards            
                

def getScore(board_numbers, called):
    score = 0
    for num in board_numbers:
        if num not in called:
            score += int(num) 
    return score                              

called = []
rounds = []
won_rounds = []

for number in numbers:
    board_list = boards;
    called.append(number)
    winning_boards = checkWin(called, board_list, won_rounds)
    if len(winning_boards) > 0:
        for win in winning_boards:
            rounds.append(win)
            won_rounds.append(win['board'])

called_list = []
last = rounds[-1]

last_num = last['number']
for num in numbers:
    if num == last_num:
        called_list.append(num)
        break
    else:
        called_list.append(num)

board = boards[last['board']]
board_numbers = boardNumbers(board)
score = getScore(board_numbers, called_list)
total = score * int(last_num)

print(score, last_num, total)


sys.stdout = orig_stdout
output.close()