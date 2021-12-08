input_file = open("input.txt", "r")
output_file = open("out.txt", "w")
lines = input_file.readlines()

digits_array = []

values = {
    'a': 333,
    'b': 114,
    'c': 5,
    'd': 215,
    'e': 57,
    'f': 30,
    'g': 2
}

for line in lines:
    sections = line.split(' | ')
    inputs = sections[0].strip().split()
    outputs = sections[1].strip().split()
    digits_array.append((inputs, outputs))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def calcValue(input):
    sum = 0;
    for char in list(input):
        sum += values[char]
    return sum    

def sortSixes(digits6, four, seven):
    nine = ''
    six = ''
    zero = ''
    for digit in digits6:
        if len(intersection(digit, four)) == 4:
            nine = digit
        if len(intersection(digit, seven)) == 2:
            six = digit
    digits6.remove(nine)
    digits6.remove(six)
    zero = digits6[0]
    return((zero, six, nine))

def sortFives(digits5, four, seven):
    two = ''
    three = ''
    five = ''
    for digit in digits5:
        if len(intersection(digit, four)) == 2:
            two = digit
        if len(intersection(digit,seven)) == 3:
            three = digit
    digits5.remove(two)
    digits5.remove(three)
    five = digits5[0]        
    return((two, three, five))

def decodeDigits(input_list):
    mapping = {}
    digits5 = []
    digits6 = []
    for input in input_list:
        if len(input) == 2:
            mapping['1'] = input
        if len(input) == 3:
            mapping['7'] = input             
        if len(input) == 4:
            mapping['4'] = input 
        if len(input) == 7:
            mapping['8'] = input
        if len(input) == 5:
            digits5.append(input)
        if len(input) == 6:
            digits6.append(input)        

    #print(mapping)
    sixes = sortSixes(digits6, mapping['4'], mapping['7'])
    mapping['0'] = sixes[0]
    mapping['6'] = sixes[1]
    mapping['9'] = sixes[2]

    fives = sortFives(digits5, mapping['4'], mapping['7']) 
    mapping['2'] = fives[0]
    mapping['3'] = fives[1]
    mapping['5'] = fives[2]

    value_map = {}
    for key, map in mapping.items():
        value_map[calcValue(map)] = key 
    return value_map   

numbers = []
for digits in digits_array:
    codes = decodeDigits(digits[0])
    print(len(codes), file=output_file)
    number = ''
    for no in digits[1]:
        val = calcValue(no)
        number += codes[val]
    numbers.append(int(number))


print(sum(numbers))
 
