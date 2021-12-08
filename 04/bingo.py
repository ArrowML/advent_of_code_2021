import sys

orig_stdout = sys.stdout
input = open('input.txt', 'r')
output = open('out.txt', 'w')
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

def checkWin(called, boards):
    for index, board in enumerate(boards, start=0):
        for row in board:
            inter = intersection(called, row)
            if len(inter) == 5:
                return index
    return -1

def getScore(board_numbers, called):
    score = 0
    for num in board_numbers:
        if num not in called:
            print(num)
            score += int(num) 
    return score                              

called = []
for number in numbers:
    called.append(number)
    win = checkWin(called, boards)
    if win > -1:
        last_num = int(called[-1])
        board = boards[win]
        board_numbers = boardNumbers(board)
        score = getScore(board_numbers, called)
        total = score * last_num
        print(win, score, last_num, total)
        break
    else:
        continue    

sys.stdout = orig_stdout
output.close()