import sys

depth_array = []
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

with open('input.txt') as file:
    for line in file:
        depth_array.append(int(line.strip()))

increase_count = 0
depths = [] 
for count in range(len(depth_array)):

    if count > 0:
        if depth_array[count - 1] < depth_array[count]:
            increase_count = increase_count + 1
            tracker = {
                "depth":depth_array[count],
                "type":"increase",
                "count":increase_count
            }
            depths.append(tracker)
        elif depth_array[count - 1] > depth_array[count]:    
            tracker = {
                "depth":depth_array[count],
                "type":"decrease",
                "count":increase_count
            }
            depths.append(tracker)
            depths.append(tracker)
        else:
            tracker = {
                "depth":depth_array[count],
                "type":"no change",
                "count":increase_count
            }
    else:
        tracker = {
            "depth":depth_array[0],
            "type":"start",
            "count":increase_count
        }
        depths.append(tracker)

    print(tracker)    

sys.stdout = orig_stdout
f.close()


                 
