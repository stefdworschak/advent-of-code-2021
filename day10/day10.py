from copy import deepcopy
from statistics import median

chars = {
    '{': {'invalid': 'close', 'closing': '}'},
    '}': {'invalid': 'open', 'closing': '{'},
    '(': {'invalid': 'close', 'closing': ')'},
    ')': {'invalid': 'open', 'closing': ')'},
    '[': {'invalid': 'close', 'closing': ']'},
    ']': {'invalid': 'open', 'closing': '['},
    '<': {'invalid': 'close', 'closing': '>'},
    '>': {'invalid': 'open', 'closing': '<'},
}

tags = {'open': ['{', '[', '(', '<'], 'close': ['}', ']', ')', '>']}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

points_cl2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def is_incomplete(line):
    for i, l in enumerate(list(line)):
        _type = chars[l]['invalid']
        try:
            if line[i+1] in tags[_type]:
                return False, line[i+1]
        except:
            return True, None
    return True, None

def has_errors(line):
    prev_line = deepcopy(line)
    while line:
        line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        if len(line) == len(prev_line):
            break
        prev_line = deepcopy(line)
    
    if not line:
        return False

    is_complete, invalid_char = is_incomplete(line)
    return (not is_complete), invalid_char, line



def challenge1(filepath):
    data = open(filepath).read().split('\n')
    total_points = 0
    for d in data:
        _has_errors, error, remaining_line = has_errors(d)
        if _has_errors:
            total_points += points[error]
    return total_points


def get_line_points(line):
    _line = list(reversed(list(line)))
    closing = ''.join([chars[c]['closing'] for c in _line])
    total_points = 0
    for cl in closing:
        total_points = total_points * 5 + points_cl2[cl]
    return total_points

def challenge2(filepath):
    data = open(filepath).read().split('\n')
    total_points = []
    for d in data:
        _has_errors, error, remaining_line = has_errors(d)
        if not _has_errors:
            points = get_line_points(remaining_line)
            total_points.append(points)
    return median(total_points)

if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day10/day10.txt')}")
    print(f"Challenge 2 Result: {challenge2('day10/day10.txt')}")
