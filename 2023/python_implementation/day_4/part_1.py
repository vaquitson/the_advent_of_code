with open('input.txt') as f:
    tot = 0
    for line in f:
        cur_win_set = set()
        cur_num_set = set()

        line = line.replace('\n', '')
        line = line.split(':')
        temp = line[1].split('|')

        winning_part = temp[0]
        your_numbers = temp[1]
        # transform ro numbers
        winning_list_numbers = winning_part.split(' ')
        for num in winning_list_numbers:
            if num != '':
                cur_win_set.add(num)
        your_list_numbers = your_numbers.split(' ')
        for num in your_list_numbers:
            if num != '':
                cur_num_set.add(num)
        intersec = len(cur_win_set & cur_num_set)
        if intersec > 0:
            points = 2**(intersec-1)
            tot += points
        

print(tot)
                