input_file = open("input_small.txt","r")
output_file = open("out1.txt", "w")

lines = input_file.readlines()

open_char_list = ['(', '[', '{', '<']
close_char_list = [')', ']', '}', '>']

test = []
for line in lines:
    char_counts = {
        '(':0,
        '[':0,
        '{':0,
        '<':0,
        ')':0,
        ']':0,
        '}':0,
        '>':0
    }
    for char in list(line.strip()):
        if char in open_char_list:
            char_counts[char] += 1
        elif char in close_char_list:
            char_counts[char] -= 1
    counts = {
        'round': char_counts['('] + char_counts[')'],
        'sqaure': char_counts['['] + char_counts[']'],
        'curly': char_counts['{'] + char_counts['}'],
        'case': char_counts['<'] + char_counts['>'],
    }        

    test.append(counts)

for counts in test:
    print(counts)

