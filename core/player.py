from core.board import Board
from random import randint
from core.exceptions import *


class Player:
    """Класс игрока"""
    def __init__(self, board: Board, log: bool = True, symb: str = "x"):
        self.board = board
        self.log = log
        self.symb = symb

    def ask(self) -> tuple[int, int]:
        """Спрашивет игрока, в какую клеетку произвести выстрел"""
    
    def move(self) -> bool:
        """Ход игрока. Если игрок ввел неверные данные, ход начинается заново"""
        while True:
            try:
                x, y = self.ask()
                return self.board.set_mark(x, y, self.symb)
            except (OutOfBoundException, AlreadyMarkedDotException) as error:
                if self.log:
                    print(error)
            except ValueError as error:
                if self.log:
                    print("Координаты введены некорректно!")


class User(Player):
    """Класс пользователя"""

    def ask(self) -> tuple[int, int]:
        x, y = map(int, input(
            "Введите координаты ячейки через пробел: "
        ).split())
        return x, y


class AI(Player):
    """Класс игрового бота"""

    def ask(self) -> tuple[int, int]:
        return randint(1, self.board.size), randint(1, self.board.size)
