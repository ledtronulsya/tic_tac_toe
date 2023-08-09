import sys
from core.board import Board
from core.player import User, AI
from time import sleep


class Game:
    """Класс игры"""
    def __init__(self) -> None:
        self.board = Board()
        self.player = User(self.board, symb="x")
        self.ai = AI(self.board, symb="o", log=False)

    def start(self):
        """Начало игры"""
        self.greet()
        self.loop()

    def greet(self):
        """Приветствие игрока"""
        print("""Привет! Это игра 'Крестики-нолики'. 
Вы ставите крестики и ходите первым.
Чтобы сделать ход, нужно ввести координаты точки, на которой вы хотите поставить крестик.
Координаты точки задаются двумя числами, записанными через пробел - номером строки и номером столбца.""")
    
    def loop(self):
        """Игровой цикл"""
        player_move = 1
        while True:
            check_result = self.board.check_field()
            if check_result:
                print(self.board)
                if check_result == "draw":
                    print("Ничья")
                else:
                    print(f"Победил {check_result}")
                self._exit()
            
            print(self.board)
            if player_move:
                self.player.move()
            else:
                sleep(1)
                print("Противник сделал ход")
                self.ai.move()
            player_move = 1 - player_move
    
    def _exit(self):
        """Выход из игры"""
        print("Приятно было провести время!")
        sleep(3)
        sys.exit(0)