input_file = open("input.txt","r")
output_file = open("out1.txt", "w")

def parseInput(file):
    heights = []
    lines = file.readlines()
    ranges = {'x':0, 'y': 0}
    for line in lines:
        ranges['x'] = len(line)
        ranges['y'] += 1
        heights.append(list(line.strip()))

    return ((heights, ranges))

def getAdjacents(x, y, input):
    heights = input[0]
    ranges = input[1]
    values = []
    current = (int(heights[y][x]), x, y)
    values.append(current)
    if x-1 >= 0:  
        left = (int(heights[y][x-1]), x-1, y)
        values.append(left)
    if x+1 < ranges['x']:  
        right = (int(heights[y][x+1]), x+1, y)
        values.append(right)
    if y-1 >= 0:    
        top = (int(heights[y-1][x]), x, y-1)
        values.append(top)
    if y+1 < ranges['y']:  
        bottom = (int(heights[y+1][x]), x, y+1)
        values.append(bottom)
    return values

def compareAdjacents(values):
    low = (9,0,0)
    for value in values:
        if value[0] < low[0]:
            low = value
    return low
        

input = parseInput(input_file)

def getLows(low_list):
    lows = []
    for low in low_list:
        values = getAdjacents(low[1], low[2], input)
        if len(values) > 1: 
            low = compareAdjacents(values)
            if low not in lows:
                lows.append(low)
    return lows 

def getSum(low_list):
    sum = 0;
    for low in low_list:
        sum += low[0] + 1
    return sum               

lows = []
for y in range(input[1]['y']):
    for x in range(input[1]['x']):
        values = getAdjacents(x, y, input)
        low = compareAdjacents(values)
        if low not in lows:
            lows.append(low)


# need to improve this recursive function? works for now
for i in range(10):
    lows = getLows(lows)
    getLows(lows)

risk = getSum(lows)
print(risk)

