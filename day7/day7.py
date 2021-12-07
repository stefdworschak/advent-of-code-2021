import json
from collections import Counter
from copy import deepcopy

def increment_fuel(fuel, increment):
    
    if not increment:
        return fuel

    total_fuel = 0
    c = 0
    for i in range(fuel):
        total_fuel += 1 + c
        c += 1

    return total_fuel


def challenge(filepath, increment=False):
    data = [int(n) for n in open(filepath).read().split(',')]
    counted = dict(Counter(data))
    fuel_consumption = {}
    for i in range(min(data), max(data)+1):
        total_fuel = 0
        for num, _count in counted.items():
            _num = int(num)
            if _num == i:
                fuel = 0
                total_fuel += fuel
                continue

            fuel_by_1 = (_num - i) if _num > i else (i - _num)
            fuel_incremented = increment_fuel(fuel_by_1, increment)
            total_fuel += (fuel_incremented * _count)
            
        fuel_consumption[i] = total_fuel
    return min(fuel_consumption.values())
    


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge('day7/day7_test.txt')}")
    print(f"Challenge 1 Result: {challenge('day7/day7.txt', increment=True)}")
