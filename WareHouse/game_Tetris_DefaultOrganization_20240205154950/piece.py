'''
This file contains the Piece class which represents a Tetris piece.
'''
class Piece:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
    def move_left(self):
        return Piece(self.shape, self.x - 1, self.y)
    def move_right(self):
        return Piece(self.shape, self.x + 1, self.y)
    def move_down(self):
        return Piece(self.shape, self.x, self.y + 1)
    def rotate(self):
        # 假设 self.shape 是一个 4x4 矩阵
        rotated_shape = [[0 for _ in range(4)] for _ in range(4)]
        for row in range(4):
            for col in range(4):
                if row < len(self.shape) and col < len(self.shape[row]):
                    rotated_shape[col][3 - row] = self.shape[row][col]
        return Piece(rotated_shape, self.x, self.y)