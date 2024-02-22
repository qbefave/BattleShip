class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Точка ({self.x}, {self.y})'

class Ship:
    def __init__(self, start,l,o):
        self.start = start
        self.l=l
        self.o=o
        self.lives=l
    @property
    def point_list(self):
        list=[]
        for i in range(self.l):

            current_x = self.start.x
            current_y = self.start.y

            if self.o == 0:
                current_x += i
            elif self.o == 1:
                current_y +=i
            list.append(Point(current_x, current_y))
        return list

    def hitted(self, hit):
        return hit in self.point_list



s=Ship(Point(1,2),4,0)
print(s.hitted(Point(2,2)))