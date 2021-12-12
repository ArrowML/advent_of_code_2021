from time import sleep


import time

input_file = open("input.txt","r")
output_file = open("out1.txt", "w")
Lines = input_file.readlines()

def countBits(bit):
    print(bit, file=output_file)
    one_count = 0
    zero_count = 0
    highest = ''
    for line in Lines:
        line.strip()
        if int(line[bit]) == 1:
            one_count += 1

        if int(line[bit]) == 0:
            zero_count += 1       

    print(one_count, zero_count, file=output_file)
    if one_count > zero_count:
        highest = '1'

    if zero_count > one_count:
        highest = '0'

    return highest

def reverseBinary(binary):
    reverse = ''
    for char in range(len(binary)):
        if binary[char] == '0':
            reverse = reverse + '1'

        if binary[char] == '1':
            reverse = reverse + '0'
    return reverse

def binaryToDecimal(n):
    return int(n,2)


bit_string = ''        
for bit in range(12):
    count = countBits(bit)
    bit_string += count

print(bit_string)
print(reverseBinary(bit_string))

gamma = binaryToDecimal(bit_string)
epsilon = binaryToDecimal(reverseBinary(bit_string))
consumption = gamma * epsilon

print(gamma, epsilon, consumption)
