from copy import deepcopy
from statistics import median


def challenge1(filepath):
    data = open(filepath).read().split('\n')
    print(data)


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day11/day11_test.txt')}")
    # print(f"Challenge 2 Result: {challenge2('day10/day10.txt')}")
