from collections import Counter
from copy import deepcopy


class Fish():
    def __init__(self, population):
        self.population = population
    
    def add_day(self):
        zeros = self.population.pop('0') if '0' in self.population else 0
        for k, v in deepcopy(self.population).items():
            new_key = int(k) - 1
            self.population[k] -= 1 * v
            self.population.setdefault(str(new_key), 0)
            self.population[str(new_key)] += 1 * v
        
        if zeros:
            self.population.setdefault('6', 0)
            self.population.setdefault('8', 0)
            self.population['6'] += zeros
            self.population['8'] += zeros


def challenge(filepath, days=80):
    data = [int(n) for n in open(filepath).read().split(',')]
    fish = Fish(dict(Counter(data)))
    for d in range(days):
        fish.add_day()

    return sum([f for f in fish.population.values()])


if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge('day6/day6.txt', 80)}")
    print(f"Challenge 1 Result: {challenge('day6/day6.txt', 256)}")
