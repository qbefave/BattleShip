from exeptions import BaseExeption, OutOfFieldExeption, ShipExeption, HittedFieldExeption
from ship import Point, Ship

class Board:
    def __init__(self, hidden = False, size=6):
        self.size = size
        self.hidden = hidden

        self.count = 0

        self.field = [ ['O']*size for _ in range(size)]

        self.active=[]
        self.ships=[]

    def __str__(self):
        res=''
        res+='  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i,row in enumerate(self.field):
            res+=f'\n{i+1} | '+' | '.join(row)+' |'
        if self.hidden:
            res = res.replace('♥','O')
        return res
    def out(self, p):
        return not ((0 <= p.x < self.size) and (0 <= p.y < self.size))

    def border(self,ship,status=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for p in ship.point_list:
            for curr_x,curr_y in near:
                curr = Point(p.x+curr_x, p.y +curr_y)
                if not(self.out(curr)) and curr not in self.active:
                    if status:
                        self.field[curr.x][curr.y] = '•'
                    self.active.append(curr)

    def add_ship(self, ship):
        for p in ship.point_list:
            if self.out(p) or p in self.active:
                raise ShipExeption()
        for p in ship.point_list:
            self.field[p.x][p.y] = "♥"
            self.active.append(p)

        self.ships.append(ship)
        self.border(ship)

    def shot(self,p):
        if self.out(p):
            raise OutOfFieldExeption

        if p in self.active:
            raise HittedFieldExeption

        self.active.append(p)

        for ship in self.ships:
            if ship.hitted(p):
                ship.lives -=1
                self.field[p.x][p.y]='X'
                if ship.lives==0:
                    self.count+=1
                    self.border(ship,status=True)
                    print("Убил")
                    return False
                else:
                    print('Ранил')
                    return False
        self.field[p.x][p.y] = '•'
        print('Мимо')
        return False
    def begin(self):
        self.active=[]


# b=Board()
# b.add_ship(Ship(Point(1,2),4,0))
# print(b)