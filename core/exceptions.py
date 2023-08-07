class OutOfBoundException(Exception):
    """Исключение, возникающее при попытке поставть точку вне поля"""
    def __init__(self, x: int, y: int):
        msg = f"Точка с координатами ({x}, {y}) выходит за пределы поля"
        super().__init__(msg)


class AlreadyMarkedDotException(Exception):
    """Исключение, возникающее, когда игрок пытается выстрелить в ту точку, которая уже открыта"""
    def __init__(self, x: int, y: int):
        msg = f"Точка с координатами ({x}, {y}) уже помечена"
        super().__init__(msg)
