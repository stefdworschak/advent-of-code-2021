from copy import deepcopy

from utils import read

navigation = {
    'horizontal': 0,
    'depth': 0,
    'aim': 0,
}


def challenge1(filepath):
    instructions = read(filepath)
    _navigation = deepcopy(navigation)
    for instruction in instructions:
        direction, amount = instruction.split(' ')
        if direction == 'forward':
            _navigation['horizontal'] += float(amount)
        elif direction == 'down':
            _navigation['depth'] += float(amount)
        elif direction == 'up':
            _navigation['depth'] -= float(amount)
        else:
            print(direction)
    
    print(_navigation)
    return _navigation['horizontal'] * _navigation['depth']


def challenge2(filepath):
    instructions = read(filepath)
    _navigation = deepcopy(navigation)
    for instruction in instructions:
        direction, amount = instruction.split(' ')
        if direction == 'down':
            _navigation['aim'] += float(amount)
        elif direction == 'up':
            _navigation['aim'] -= float(amount) 
        elif direction == 'forward':
            _navigation['horizontal'] += float(amount)
            _navigation['depth'] += (_navigation['aim'] * float(amount))
        else:
            print(direction)
    
    print(_navigation)
    return _navigation['horizontal'] * _navigation['depth']


if __name__== '__main__':
    print(challenge1('day2/day2.txt'))
    print(challenge2('day2/day2.txt'))