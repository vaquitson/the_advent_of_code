baondries = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as f:
    tot = 0
    for game in f:
        game = game.replace(':', ';')
        game = game.replace('\n', '')

        split_game = game.split(';')
        game_id = split_game[0].split(' ')[1]
        valid_game = True
        for cube_set_index in range(len(split_game)-1):
            if not valid_game:
                break
            cube_set_index += 1
            cur_cube_set = split_game[cube_set_index]
            for cubes in cur_cube_set.split(','):
                cubes_split = cubes.split(' ')
                cube_color = cubes_split[2]
                cube_num = int(cubes_split[1])
                if baondries[cube_color] < cube_num:
                    valid_game = False
                    break
        if valid_game:
            tot += int(game_id)
    print(tot)