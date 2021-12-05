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
        return 'diagonal'
    
    def get_coordinates(self, direction):
        if direction == 'vertical':
            return min(self.y0, self.y1), max(self.y0, self.y1)
        elif direction == 'horizontal':
            return min(self.x0, self.x1), max(self.x0, self.x1)
        else:
            return (self.x0, self.y0), (self.x1, self.y1)

    def walk_straight(self, start, end, direction):
        for i in range(start, end + 1):
            if direction == 'vertical':
                self.points.setdefault((self.x0, i), 0)
                self.points[(self.x0, i)] += 1
            else:
                self.points.setdefault((i, self.y0), 0)
                self.points[(i, self.y0)] += 1
    
    def walk_diagonally(self, start, end):
        x_start, y_start = start
        x_end, y_end = end
        self.points.setdefault((x_start, y_start), 0)
        self.points[(x_start, y_start)] += 1
        while (x_start != x_end and y_start != y_end):
            if x_start < self.x1:
                x_start += 1
            else:
                x_start -= 1
            
            if y_start < self.y1:
                y_start += 1
            else:
                y_start -= 1

            self.points.setdefault((x_start, y_start), 0)
            self.points[(x_start, y_start)] += 1


    def walk_line(self, start, end, direction):
        if direction == 'diagonal':
            self.walk_diagonally(start, end)
        else:
            self.walk_straight(start, end, direction)


def challenge(filepath):
    data = [[r.strip() for r in d.split(' -> ')] for d in read(filepath)]
    for d in data:
        line = Line(d)
        direction = line.get_direction()
        start, end = line.get_coordinates(direction)
        line.walk_line(start, end, direction)
            
    return sum([1 for l in line.points.values()
                if l >= 2])
    

if __name__ == '__main__':
    print(f"Challenge 1 Result: {challenge('day5/day5.txt')}")
    print(f"Challenge 2 Result: {challenge('day5/day5.txt')}")
