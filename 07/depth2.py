with open("input.txt") as file:
    inputs = [int(x) for x in file.read().split(",")]

def getDepthList(inout_list):
    inout_list.sort()
    min = inout_list[0]
    max = inout_list[-1]
    return list(range(min, max))

def calcFuel(loc, depth, step_table):
    steps = 0
    if loc >= depth:
        steps += loc - depth
    else:
        steps += depth - loc
    fuel = 0
    if steps > 0:
        if steps in step_table.keys():
            return step_table[steps]
        else:
            for nr in range(steps):
                fuel += nr + 1 
            step_table[steps] = fuel            
    return fuel


def getFuelUsage(inputs, depths):
    fuel_use = {}
    step_table = {}
    for depth in depths:
        fuel = 0
        for loc in inputs:
            fuel += calcFuel(loc, depth, step_table)   
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


        



    
        