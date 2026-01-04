numbers = [f'{i}' for i in range(10)]
with open('input.txt', 'r') as f:
    tot = 0
    for line in f:
        line = line.replace('\n', '')
        cur_nums = ''
        for i in range(len(line)):
            if line[i] in numbers:
                cur_nums += line[i]
                break
        
        for j in range(len(line)):
            if line[len(line)-1-j] in numbers:
                cur_nums += line[len(line)-1-j]
                break
        tot += int(cur_nums)
        cur_nums = ''
    print(tot)