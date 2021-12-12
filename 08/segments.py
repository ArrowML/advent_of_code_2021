input_file = open("input.txt","r")
output_file = open("out1.txt", "w")
lines = input_file.readlines()

outputs = []

digit_mapping = [2,3,4,7]

for line in lines:
    segs = line.split(' | ')
    outputs.append(segs[1].strip())

count = 0
for output in outputs:
    digits = output.split()
    for digit in digits:
        if len(digit) in digit_mapping:
            count += 1

print(count)
