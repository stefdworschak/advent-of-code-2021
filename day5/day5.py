import re
from utils import read

class Line():
    points = {}    

    def __init__(self, d):
        self.x0, self.y0 = [int(n) for n in d[0].split(',')]
        self.x1, self.y1 = [int(n) for n in d[1].split(',')]
    
    def get_direction(self):
        if self.x0 == self.x1:
            return 'vertical'
        elif self.y0 == self.y1:
            return 'horizontal'
        return
    
    def get_coordinates(self, direction):
        if direction == 'vertical':
            return min(self.y0, self.y1), max(self.y0, self.y1)
        return min(self.x0, self.x1), max(self.x0, self.x1)
    
    def walk_line(self, start, end, direction):
        for i in range(start, end + 1):
            if direction == 'vertical':
                self.points.setdefault((self.x0, i), 0)
                self.points[(self.x0, i)] += 1
            else:
                self.points.setdefault((i, self.y0), 0)
                self.points[(i, self.y0)] += 1


def challenge1(filepath):
    data = [[r.strip() for r in d.split(' -> ')] for d in read(filepath)]
    # d = data[0]
    for d in data:
        line = Line(d)
        direction = line.get_direction()
        if not direction:
            continue
        print(d)
        start, end = line.get_coordinates(direction)
        line.walk_line(start, end, direction)
            
    print(sum([1 for l in line.points.values()
               if l >= 2]))
    # print(line.points)

    

if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge1('day5/day5.txt')}")
    # print(f"Challenge 2 Result: {challenge('day4/day4.txt', False)}")