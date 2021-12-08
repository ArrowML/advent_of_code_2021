import sys

inputs = []
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

with open('input.txt') as file:
    for line in file:
        line_parts = line.split(' ')
        vector = (line_parts[0], int(line_parts[1].strip()))
        inputs.append(vector)


depth = 0
distance = 0

for vector in inputs:
    if vector[0] == 'forward':
        distance = distance + vector[1]

    if vector[0] == 'down':
        depth = depth + vector[1]

    if vector[0] == 'up':
        depth = depth - vector[1]

print('depth: ', depth)
print('distance: ',distance)                
multiple = depth * distance
print('multiple: ', multiple)

sys.stdout = orig_stdout
f.close()