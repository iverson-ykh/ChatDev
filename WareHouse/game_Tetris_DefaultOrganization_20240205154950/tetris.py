'''
This file contains the Tetris class which represents the game logic and GUI.
'''
import tkinter as tk
import random
from piece import Piece
class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        self.canvas = tk.Canvas(self.root, width=300, height=600, bg="black")
        self.canvas.pack()
        self.score = 0
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = self.generate_piece()
        self.next_piece = self.generate_piece()
        self.is_game_over = False
        self.draw_board()
    def start(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_piece)
        self.root.after(1000, self.update)
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.draw_block(col, row, "blue")
        if self.current_piece:
            for row in range(len(self.current_piece.shape)):
                for col in range(len(self.current_piece.shape[row])):
                    if self.current_piece.shape[row][col]:
                        self.draw_block(self.current_piece.x + col, self.current_piece.y + row, "red")

    def draw_block(self, x, y, color):
        self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill=color)

    def update(self):
        if not self.is_game_over:
            if self.current_piece is None:
                self.current_piece = self.next_piece
                self.next_piece = self.generate_piece()
                if self.check_collision(self.current_piece):
                    self.is_game_over = True
            else:
                self.move_down()
        self.draw_board()
        self.root.after(1000, self.update)
    def move_left(self, event=None):
        if not self.is_game_over and self.current_piece is not None:
            new_piece = self.current_piece.move_left()
            if not self.check_collision(new_piece):
                self.current_piece = new_piece
    def move_right(self, event=None):
        if not self.is_game_over and self.current_piece is not None:
            new_piece = self.current_piece.move_right()
            if not self.check_collision(new_piece):
                self.current_piece = new_piece
    def move_down(self, event=None):
        if not self.is_game_over and self.current_piece is not None:
            new_piece = self.current_piece.move_down()
            if not self.check_collision(new_piece):
                self.current_piece = new_piece
            else:
                self.place_piece()
    def rotate_piece(self, event=None):
        if not self.is_game_over and self.current_piece is not None:
            new_piece = self.current_piece.rotate()
            if not self.check_collision(new_piece):
                self.current_piece = new_piece
    def check_collision(self, piece):
        if piece is None:
            return False
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[0])):
                if piece.shape[row][col] and (piece.y + row >= 20 or piece.x + col < 0 or piece.x + col >= 10 or self.board[piece.y + row][piece.x + col]):
                    return True
        return False
    def place_piece(self):
        for row in range(len(self.current_piece.shape)):
            for col in range(len(self.current_piece.shape[row])):
                if self.current_piece.shape[row][col]:
                    self.board[self.current_piece.y + row][self.current_piece.x + col] = 1
        self.clear_lines()
        self.current_piece = None
    def clear_lines(self):
        lines_cleared = 0
        new_board = []
        for row in range(20):
            if not all(self.board[row]):
                new_board.append(self.board[row])
            else:
                lines_cleared += 1
        while len(new_board) < 20:
            new_board.insert(0, [0] * 10)
        self.board = new_board
        self.score += lines_cleared * 100
    def generate_piece(self):
        shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]]
        ]
        shape = random.choice(shapes)
        x = (10 - len(shape[0])) // 2
        y = 0
        return Piece(shape, x, y)