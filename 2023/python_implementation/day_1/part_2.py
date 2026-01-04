valid_nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt', 'r') as f:
    tot = 0
    for line in f:
        line = line.replace('\n', '')
        first_num = None
        last_num = None
        for i in range(len(line)):
            first_2_last = line[:i+1]
            last_2_first = line[len(line)-i-1:]
            for key, value in valid_nums.items():
                if first_num is None:
                    if (key in first_2_last) or (value in first_2_last):
                        first_num = value
                if last_num is None:
                    if (key in last_2_first) or (value in last_2_first):
                        last_num = value
            if first_num is not None and last_num is not None:
                break
        tot += int(f'{first_num}{last_num}')
    print(tot)