input_file = open("input.txt","r")
output_file = open("out2.txt", "w")
Lines = input_file.readlines()


def filterList(lines, bit, highest):
    filtered_list = []
    for line in lines:
        if line[bit] == highest:
            filtered_list.append(line.strip())
    return filtered_list 
      
def binaryToDecimal(n):
    return int(n,2)    

def findOxygen(bit, lines):
    one_count = 0
    zero_count = 0
    highest = ''
    for line in lines:
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

    if one_count == zero_count:
        highest = '1'    

    filtered_lines = filterList(lines, bit, highest)
    print(len(filtered_lines), file=output_file)
    if len(filtered_lines) > 1:
        print(filtered_lines, file=output_file)
        filtered_lines = findOxygen(bit + 1, filtered_lines)

    return filtered_lines

def findCO2(bit, lines):
    one_count = 0
    zero_count = 0
    highest = ''
    for line in lines:
        line.strip()
        if int(line[bit]) == 1:
            one_count += 1

        if int(line[bit]) == 0:
            zero_count += 1 

    print(one_count, zero_count, file=output_file)              

    if one_count > zero_count:
        lowest = '0'

    if zero_count > one_count:
        lowest = '1'

    if one_count == zero_count:
        lowest = '0'    

    filtered_lines = filterList(lines, bit, lowest)
    print(len(filtered_lines), file=output_file)
    if len(filtered_lines) > 1:
        print(filtered_lines, file=output_file)
        filtered_lines = findCO2(bit + 1, filtered_lines)

    return filtered_lines    

oxygen_bin = findOxygen(0, Lines)
co2_bin = findCO2(0, Lines)

oxygen = binaryToDecimal(oxygen_bin[0])
co2 = binaryToDecimal(co2_bin[0])
rating = oxygen * co2
print(oxygen, co2, rating)










        


