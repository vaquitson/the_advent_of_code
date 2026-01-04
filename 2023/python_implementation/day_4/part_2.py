with open('input.txt') as f:
    tot = 0
    line_list = f.readlines()
    for line in line_list:
        cur_win_set = set()
        cur_num_set = set()

        line = line.replace('\n', '')
        line = line.split(':')
        temp = line[1].split('|')

        card_number = int(line[0].split(' ')[-1])
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
            for add in range(1, intersec+1):
                line_list.append(line_list[card_number+add-1])

print(len(line_list))
                