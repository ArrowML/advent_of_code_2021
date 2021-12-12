with open("input_small.txt") as file:
    inputs = [int(x) for x in file.read().split(",")]

def getDepthList(inout_list):
    inout_list.sort()
    min = inout_list[0]
    max = inout_list[-1]
    return list(range(min, max))

def getFuelUsage(inputs, depths):
    fuel_use = {}
    for depth in depths:
        fuel = 0
        for loc in inputs:
            if loc >= depth:
                fuel += loc - depth
            else:
                fuel += depth - loc
        fuel_use[depth] = fuel
    return fuel_use 

def getBestFuel(usage):
    first_key = list(usage.keys())[0]
    first_value = list(usage.values())[0]
    best = (first_key, first_value)
    for key, use in usage.items():
        if use < best[1]:
            best = (key, use)
    return best        

depths = getDepthList(inputs)
fuel_usage = getFuelUsage(inputs, depths);
best = getBestFuel(fuel_usage)
print(best)


        



    
        