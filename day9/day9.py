from copy import deepcopy

MOVES = {
    'left': None,
    'right': None,
    'up': None,
    'down': None,
}


def move(coords, direction):
    i, j = coords
    if direction == 'left':
        return [i, j-1]
    elif direction == 'right':
        return [i, j+1]
    elif direction == 'up':
        return [i-1, j]
    else:
        return [i+1, j]
            

def get_safely(data, i1, i2):
    i1 = None if i1 < 0 else int(i1)
    i2 = None if i2 < 0 else int(i2)
    try:
        return data[i1][i2]
    except IndexError:
        return None
    except TypeError:
        return None


def get_moves(data, i, j):
    moves = deepcopy(MOVES)
    moves['left'] = get_safely(data, i, j-1)
    moves['right'] = get_safely(data, i, j+1)
    moves['up'] = get_safely(data, i-1, j)
    moves['down'] = get_safely(data, i+1, j)
    return moves


def check_smallest(element, moves):
    return any(int(i) <= int(element) for i in moves.values() if i is not None)


def check_risk_levels(data):
    risk_levels = []
    basins = []
    for i, row in enumerate(data):
        for j, element in enumerate(list(row)):
            moves = get_moves(data, i, j)
            if not check_smallest(element, moves):
                risk_levels.append(int(element) + 1)
                basin = {
                    'coords': [i, j],
                    'moves': moves,
                    'value': int(element)
                }
                basins.append(basin)
    return risk_levels, basins


def challenge1(filepath):
    data = open(filepath).read().split('\n')
    risk_levels, _ = check_risk_levels(data)
    return sum(risk_levels)


def find_basin(basins, data, used_coords=[], results=[]):
    if not basins:
        return results

    basin = basins.pop(0)
    used_coords.append(basin['coords'])
    results.append(basin['value'])
    next_up = [k for k,i in basin['moves'].items() 
               if i is not None and basin['value'] < int(i) and int(i) != 9]
    for n in next_up:
        x, y = move(basin['coords'] ,n)
        if [x, y] in used_coords:
            continue
        moves = get_moves(data, x, y)
        basins.append({
            'coords': [x, y],
            'moves': moves,
            'value': basin['value'] + 1,
        })
        used_coords.append([x, y])
    return find_basin(basins, data, used_coords, results)


def challenge2(filepath):
    data = open(filepath).read().split('\n')
    _, basins = check_risk_levels(data)
    basin_lengths = []
    used_cords = []
    for basin in basins:
        whole_basin = find_basin([basin], data, used_cords, [])
        basin_lengths.append(len(whole_basin))
    sorted_desc = sorted(basin_lengths, reverse=True)
    return sorted_desc[0] * sorted_desc[1] * sorted_desc[2]


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day9/day9.txt')}")
    print(f"Challenge 2 Result: {challenge2('day9/day9.txt')}")
