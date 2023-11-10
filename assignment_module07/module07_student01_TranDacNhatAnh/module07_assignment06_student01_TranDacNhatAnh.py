import numpy as np
import matplotlib.pyplot as plt

from .additionalFolder.Geometry import Vector, Point

# Tạo một bảng (hình vuông) với các ô chứa các giá trị là 0 hoặc 1 (tương ứng với màu trắng hoặc đen)
def generateBoard(size: int, colour: list[int]) -> np.ndarray:
    pass

# Truy cập vào vị trí của bảng bằng tọa độ ở dạng Point(x, y)
def getPosition(board: np.ndarray, position: Point) -> int:
    return position.y, position.x

class LangtonsAnt:
    def __init__(self, board: np.ndarray, direction: Vector, position: Point, moveHistory: list[Point]) -> None:
        self.board = board
        self.currentDirection = direction
        self.currentPosition = position
        self.history = moveHistory
    
    # Thực hiện một bước di chuyển
    def move(self):
        self.history.append(self.currentPosition)
        self.board[getPosition(self.currentPosition)] = 1 - self.board[getPosition(self.currentPosition)]
        if getPosition(board = self.board, position = self.currentPosition) == 1:
            self.currentDirection = self.currentDirection.getPerpendicular()
            self.currentPosition = self.currentPosition.vectorAdd(self.currentDirection)
        else:
            self.currentDirection = -self.currentDirection.getPerpendicular()
            self.currentPosition = self.currentPosition.vectorAdd(self.currentDirection)
        return self
    
    # Phần này em muốn show trạng thái của bảng ở "thời điểm hiện tại" mà chưa biết làm ;v;
    def show(self):
        pass

    def __repr__(self) -> str:
        return f'Position: {self.currentPosition}, Direction: {self.currentDirection}, History: {self.history}'