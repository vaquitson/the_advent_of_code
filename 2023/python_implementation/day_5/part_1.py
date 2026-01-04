def print_s(n, spaced=False):
    print(n)
    print('--------------------------')
    if spaced:
        print()


def get_ranges_from_map(mapping):
    '''
    seed-to-soil map:
    // mpping
    ['50 98 2', '52 50 48']
    //
    '''
    range_list = []
    for ranges in mapping:
        ranges = ranges.split(' ')
        ranges = list(map(lambda n: int(n), ranges))
        destination_range = (ranges[0], ranges[0] + ranges[2]-1)
        source_reange = (ranges[1], ranges[1] + ranges[2]-1)
        range_list.append((source_reange, destination_range))
    return range_list

def convert_src_to_dest(range_list: list, source: list):
    transformation = []
    for num in source:
        find_in_range = False
        for ranges in range_list:
            source_reange, destination_range = ranges
            if source_reange[0] <= num <= source_reange[1]:
                dest_num = destination_range[0] + num - source_reange[0]
                transformation.append(dest_num)
                print(f'source {num}: {dest_num}')
                find_in_range = True
                break
        if not find_in_range:
            transformation.append(num)
            print(f'source {num}: {num}')
    print('-----------------------------')
    return transformation
        


with open('input.txt') as f:
    f = f.read().split('\n\n')

    src = f[0].split(' ')
    src = src[1:]
    src = list(map(lambda n: int(n), src))

    # iterate trough maps
    for i in range(len(f)-1):
        i += 1
        cur_map = f[i]
        cur_map = cur_map.split('\n')
        cur_map = cur_map[1:]
        range_list = get_ranges_from_map(cur_map)
        src = convert_src_to_dest(range_list, src)
    print()
    src.sort()
    print(src[0])