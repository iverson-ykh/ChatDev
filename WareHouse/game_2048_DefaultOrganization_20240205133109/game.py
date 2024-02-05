'''
This file contains the Game class which represents the 2048 game logic.
'''
import random
import tkinter as tk
class Game:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    def get_grid(self):
        return self.grid
    def get_score(self):
        return self.score
    def add_random_tile(self):
        empty_cells = []
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col] = random.choice([2, 4])
    def move_up(self):
        for col in range(4):
            for row in range(1, 4):
                if self.grid[row][col] != 0:
                    current_row = row
                    while current_row > 0 and self.grid[current_row - 1][col] == 0:
                        self.grid[current_row - 1][col] = self.grid[current_row][col]
                        self.grid[current_row][col] = 0
                        current_row -= 1
                    if current_row > 0 and self.grid[current_row - 1][col] == self.grid[current_row][col]:
                        self.grid[current_row - 1][col] *= 2
                        self.score += self.grid[current_row - 1][col]
                        self.grid[current_row][col] = 0
        self.add_random_tile()
    def move_down(self):
        for col in range(4):
            for row in range(2, -1, -1):
                if self.grid[row][col] != 0:
                    current_row = row
                    while current_row < 3 and self.grid[current_row + 1][col] == 0:
                        self.grid[current_row + 1][col] = self.grid[current_row][col]
                        self.grid[current_row][col] = 0
                        current_row += 1
                    if current_row < 3 and self.grid[current_row + 1][col] == self.grid[current_row][col]:
                        self.grid[current_row + 1][col] *= 2
                        self.score += self.grid[current_row + 1][col]
                        self.grid[current_row][col] = 0
        self.add_random_tile()
    def move_left(self):
        for row in range(4):
            for col in range(1, 4):
                if self.grid[row][col] != 0:
                    current_col = col
                    while current_col > 0 and self.grid[row][current_col - 1] == 0:
                        self.grid[row][current_col - 1] = self.grid[row][current_col]
                        self.grid[row][current_col] = 0
                        current_col -= 1
                    if current_col > 0 and self.grid[row][current_col - 1] == self.grid[row][current_col]:
                        self.grid[row][current_col - 1] *= 2
                        self.score += self.grid[row][current_col - 1]
                        self.grid[row][current_col] = 0
        self.add_random_tile()
    def move_right(self):
        for row in range(4):
            for col in range(2, -1, -1):
                if self.grid[row][col] != 0:
                    current_col = col
                    while current_col < 3 and self.grid[row][current_col + 1] == 0:
                        self.grid[row][current_col + 1] = self.grid[row][current_col]
                        self.grid[row][current_col] = 0
                        current_col += 1
                    if current_col < 3 and self.grid[row][current_col + 1] == self.grid[row][current_col]:
                        self.grid[row][current_col + 1] *= 2
                        self.score += self.grid[row][current_col + 1]
                        self.grid[row][current_col] = 0
        self.add_random_tile()