import sys

depth_array = []
orig_stdout = sys.stdout
f = open('out2.txt', 'w')
sys.stdout = f

with open('input.txt') as file:
    for line in file:
        depth_array.append(int(line.strip()))

depth_sums = []        
for count in range(len(depth_array)):
    if count < len(depth_array) - 2:
        sums = depth_array[count] + depth_array[count+1] + depth_array[count+2]
        depth_sums.append(sums)  


increase_count = 0
depths = [] 
for count in range(len(depth_sums)):

    if count > 0:
        if depth_sums[count - 1] < depth_sums[count]:
            increase_count = increase_count + 1
            tracker = {
                "depth":depth_sums[count],
                "type":"increase",
                "count":increase_count
            }
            depths.append(tracker)
        elif depth_sums[count - 1] > depth_sums[count]:    
            tracker = {
                "depth":depth_sums[count],
                "type":"decrease",
                "count":increase_count
            }
            depths.append(tracker)
            depths.append(tracker)
        else:
            tracker = {
                "depth":depth_sums[count],
                "type":"no change",
                "count":increase_count
            }
    else:
        tracker = {
            "depth":depth_sums[0],
            "type":"start",
            "count":increase_count
        }
        depths.append(tracker)

    print(tracker)  

 
sys.stdout = orig_stdout
f.close()
