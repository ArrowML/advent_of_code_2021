input_file = open("input_small.txt","r")
output_file = open("out1.txt", "w")
lines = input_file.readlines()

input = lines[0].split(',')
fish_count = []
for fish in input:
    fish_count.append(int(fish))
add_fish = 0
count = 0

for day in range(18):
    for idx, fish in enumerate(fish_count):
        fish_count[idx] -= 1
        if fish_count[idx] == 0:
            add_fish += 1
            fish_count[idx] = 7        

    count = len(fish_count)

    for i in range(add_fish):
        fish_count.append(9)
    add_fish = 0  

print(count)             
