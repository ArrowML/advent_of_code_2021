import sys

orig_stdout = sys.stdout
input = open('input.txt', 'r')
output = open('out.txt', 'w')
sys.stdout = output

inputs = input.readlines()
grid = [];

def generateGrid(size):
    grid = [];
    for rows in range(size):
        row = []
        for column in range(size):
            row.append(0)
        grid.append(row)    
    return grid 

def parseCoordinates(input_lines):
    line_coordinates = []
    for line in input_lines:
        points = line.split(' -> ')
        vector = {}
        for idx, point in enumerate(points, 1):
            coo = point.split(',')
            vector['x' + str(idx)] = int(coo[0].strip())
            vector['y'+ str(idx)] = int(coo[1].strip())
        line_coordinates.append(vector)
    return line_coordinates                     


def drawHorizonal(line, grid_ref):
    x = line['x1']
    start = line['y1']
    end = line['y2']
    if line['y2'] < line['y1']:
        start = line['y2']
        end = line['y1']
    for y in range(start, end + 1):
        grid_ref[y][x] += 1

def drawVertical(line, grid_ref):
    y = line['y1']
    start = line['x1']
    end = line['x2']
    if line['x2'] < line['x1']:
        start = line['x2']
        end = line['x1']
    for x in range(start, end + 1):
        grid_ref[y][x] += 1

def drawDiagonal(line, grid_ref):

    start_x = line['x1']
    start_y = line['y1']
    x_direction = '+'
    y_direction = '+'
    length = 0
    if line['x1'] > line['x2']:
        length = line['x1'] - line['x2']
        x_direction = '-'
    else:
        length = line['x2'] - line['x1']

    if line['y1'] > line['y2']:
        y_direction = '-'
 
    for i in range(length + 1):
        grid_ref[start_y][start_x] += 1
        if x_direction == '+':
            start_x += 1
        else:
            start_x -= 1

        if y_direction == '+':
            start_y += 1
        else:
            start_y -= 1         

def plotLine(line, grid_ref):
    if line['x1'] == line['x2']:
        drawHorizonal(line, grid_ref)
    elif line['y1'] == line['y2']:
        drawVertical(line, grid_ref)
    else:   
        drawDiagonal(line, grid_ref)            


grid = generateGrid(1000)

coordinates = parseCoordinates(inputs)
for co in coordinates:
    plotLine(co, grid) 

overlap = 0
for row in grid:
    for item in row:
        if item > 1:
            overlap += 1

print(overlap)


sys.stdout = orig_stdout
output.close()