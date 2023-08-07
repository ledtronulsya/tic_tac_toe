from core.exceptions import *


class Board:
    """Класс доски"""
    def __init__(self, size: int = 3):
        self.size = size
        self.field = [["-" for _ in range(size + 1)] for _ in range(size + 1)]
        self.add_headers()

    def add_headers(self):
        """Добавляет чисел на первой строке и первом столбце"""
        self.field[0] = [" "] + list(range(1, self.size + 1))
        for row in range(1, self.size + 1):
            self.field[row][0] = row

    def __str__(self) -> str:
        """Вывод поля в консоль"""
        res = ["| " + " | ".join(map(str, row)) + " |" for row in self.field]
        return "_" * len(res[0]) + "\n" + '\n'.join(res) + "\n" + "‾" * len(res[0])
    
    def out(self, x: int, y: int) -> bool:
        """Проверка, выходит ли точка за пределы поля"""
        return not (1 <= x <= self.size and 1 <= y <= self.size)
    
    def set_mark(self, x: int, y: int, mark: str):
        """Устанавливает крестик или нолик в ячейку"""
        if self.out(x, y):
            raise OutOfBoundException(x, y)
        if self.field[x][y] != "-":
            raise AlreadyMarkedDotException(x, y)
        self.field[x][y] = mark
        return True
    
    def get_col(self, col: int) -> list[str]:
        """Возвращает столбец под номером col"""
        return [self.field[row][col] for row in range(1, self.size + 1)]
    
    def get_diag(self, main_=True):
        """Возвращает главную диагональ, если main_ = True, иначе побочную"""
        if main_:
            return [self.field[i][i] for i in range(1, self.size + 1)]
        return [self.field[i][self.size - i + 1] for i in range(1, self.size + 1)]
    
    def check_field(self) -> bool | str:
        """Проверка поля на выигрышную ситуацию"""
        player_win_flag = ai_win_flag = False
        variants = [self.field[i][1:] for i in range(1, self.size + 1)]
        variants.extend([self.get_col(i) for i in range(1, self.size + 1)])
        variants.extend([self.get_diag(), self.get_diag(False)])
        for v in variants:
            if v == ["x"] * self.size:
                player_win_flag = True
            elif v == ["o"] * self.size:
                ai_win_flag = True
        if player_win_flag:
            return "x"
        if ai_win_flag:
            return "o"
        if all(self.field[row][col] != "-" for row in range(1, self.size + 1) for col in range(1, self.size + 1)):
            return "draw"
        return False
