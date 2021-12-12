input_file = open("input_small.txt","r")
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

def updateLows(lows, current):
    if len(lows) == 0:
        lows.append(current)
        return
    for idx, low in enumerate(lows):
        if current == low:
            return
        else:
            if sameLocation(current, low):
                if current[0] < low[0]:
                    lows[idx] = current
            else:
                lows.append(current)    

def sameLocation(current, low):
    if current[1] > low[1] + 1 & current[2] > low[2] + 1:
        return True   
    return False

def getAdjacentLows(lows):
adjacent_lows = []
for idx, low in enumerate(lows):
    if 


input = parseInput(input_file)

lows = []
for y in range(input[1]['y']):
    for x in range(input[1]['x']):
        values = getAdjacents(x, y, input)
        low = compareAdjacents(values)
        if low not in lows:
            lows.append(low)


sorted = getAdjacentLows(lows)

print(sorted);

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
