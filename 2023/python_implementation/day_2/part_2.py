with open('input.txt', 'r') as f:
    tot = 0
    for game in f:
        game = game.replace(':', ';')
        game = game.replace('\n', '')
        split_game = game.split(';')
        game_id = split_game[0].split(' ')[1]

        cur_cub_max = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for cube_set_index in range(len(split_game)-1):
            cube_set_index += 1
            cur_cube_set = split_game[cube_set_index]
            for cubes in cur_cube_set.split(','):
                cubes_split = cubes.split(' ')
                cube_color = cubes_split[2]
                cube_num = int(cubes_split[1])
                if cur_cub_max[cube_color] < cube_num:
                    cur_cub_max[cube_color] = cube_num
        tot += cur_cub_max['red'] * cur_cub_max['green'] * cur_cub_max['blue']

print(tot)