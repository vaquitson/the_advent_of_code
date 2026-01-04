numbers = [str(i) for i in range(10)]


with open('input.txt', 'r') as f:
    tot = 0

    line_list = f.readlines()

    # get ride of up and down edge cases
    add_line = ''.join(['.' for _ in range(len(line_list[0])-1)])
    add_line += '\n'
    line_list.insert(0, add_line)
    line_list.append(add_line)

    for row_index in range(len(line_list)):
        line = line_list[row_index]
        line = line.replace('\n', '.')
        line = '.' + line

        number_indexes = [[]]

        # get number sequences
        for char_index in range(len(line)-1):
            char = line[char_index]
            if char in numbers:
                number_indexes[-1].append(str(char_index))
                if line[char_index+1] not in numbers:
                    number_indexes.append([])
        number_indexes.pop()

        # check surraundings
        for number_i in number_indexes:
            if len(number_i) == 0:
                continue
            valid_num = False
            for row_add in range(-1, 2):
                if valid_num:
                    break
                cur_row = line_list[row_index+row_add]
                cur_row = cur_row.replace('\n', '.')
                cur_row = '.' + cur_row

                for index in range(int(number_i[0])-1, int(number_i[-1])+2):
                    to_check = cur_row[index]
                    if to_check not in numbers and to_check != '.':
                        valid_num = True
                        break
            if valid_num:
                num = ''
                for number in number_i:
                    num += line[int(number)]
                tot += int(num)
print(tot)
                