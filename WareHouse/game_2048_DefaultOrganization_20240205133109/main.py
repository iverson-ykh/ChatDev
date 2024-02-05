'''
This is the main file for the 2048 game.
'''
import tkinter as tk
from game import Game
class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2048 Game")
        self.geometry("400x400")
        self.game = Game()
        self.create_widgets()
    def create_widgets(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=10)
        self.tiles = []
        for row in range(4):
            row_tiles = []
            for col in range(4):
                tile = tk.Label(self.grid_frame, width=10, height=5, relief="solid", borderwidth=1)
                tile.grid(row=row, column=col, padx=5, pady=5)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)
        self.score_label = tk.Label(self, text="Score: 0")
        self.score_label.pack()
        self.bind("<Key>", self.handle_keypress)
    def update_grid(self):
        grid = self.game.get_grid()
        for row in range(4):
            for col in range(4):
                value = grid[row][col]
                if value == 0:
                    self.tiles[row][col].config(text="")
                else:
                    self.tiles[row][col].config(text=str(value))
        self.score_label.config(text="Score: " + str(self.game.get_score()))
    def handle_keypress(self, event):
        if event.keysym == "Up":
            self.game.move_up()
        elif event.keysym == "Down":
            self.game.move_down()
        elif event.keysym == "Left":
            self.game.move_left()
        elif event.keysym == "Right":
            self.game.move_right()
        self.update_grid()
if __name__ == "__main__":
    game_window = GameWindow()
    game_window.mainloop()