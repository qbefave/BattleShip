from exeptions import BaseExeption
from ship import Point, Ship
from board import Board
from random import randint

class Player:
    def __init__(self,board, enemy):
        self.board=board
        self.enemy=enemy
    def ask(self):
        raise NotImplemented
    def turn(self):
        while True:
            try:
                aim = self.ask()
                repeat = self.enemy.shot(aim)
                return repeat
            except BaseExeption as e:
                print(e)

class AI(Player):
    def ask(self):
        p = Point(randint(0,5), randint(0, 5))
        print(f"Ход компьютера: {p.x+1} {p.y+1}")
        return p


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue
            if ( int(x) > 6 and int(x) < 0) or  (int(y) > 6 and int(y) <0):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Point(x - 1, y - 1)