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

input = parseInput(input_file)    

def getAdjacents(x, y, list):
    heights = input[0]
    ranges = input[1]
    values = []
    if x-1 >= 0:  
        left = (int(heights[y][x-1]), x-1, y)
        if left[0] < 9 and left not in list:
            values.append(left)
    if x+1 < ranges['x']:  
        right = (int(heights[y][x+1]), x+1, y)
        if right[0] < 9 and right not in list:
            values.append(right)
    if y-1 >= 0:    
        top = (int(heights[y-1][x]), x, y-1)
        if top[0] < 9 and top not in list:
            values.append(top)
    if y+1 < ranges['y']:  
        bottom = (int(heights[y+1][x]), x, y+1)
        if bottom[0] < 9 and bottom not in list:
            values.append(bottom)
    return values


def getPoints(point_list, accum_list = []):
    if len(point_list) > 0:
        for point in point_list:
            if point not in accum_list:
                accum_list.append(point)
                adjacents = getAdjacents(point[1], point[2], accum_list)
                if len(adjacents) > 0:
                    getPoints(adjacents, accum_list)
        return accum_list;            
                    
def getStats(basin):
    count = 0
    value = 0
    for point in basin:
        count += 1
        value += point[0]
    return (count,value)    
    

height_map = []
for y in range(input[1]['y']):
    for x in range(input[1]['x']):
        current = (int(input[0][y][x]), x, y)
        height_map.append(current)

basins = []
for height in height_map:
    if height[0] < 9:
        point = [height]   
        basin = getPoints(point, [])
        stats = getStats(basin)
        if stats not in basins:
            basins.append(stats)


sorted_basins = sorted(basins, key=lambda tup: tup[0], reverse=True)
total = 1  
for i in range(3):
    total *= sorted_basins[i][0]

print(total)    
    
