import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ta Te Ti")
        self.root.resizable(False, False)  # Evita que la ventana sea redimensionable

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.x_wins = 0
        self.o_wins = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                                              command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.x_label = tk.Label(root, text="X wins: 0", font=("Helvetica", 16))
        self.x_label.grid(row=3, column=0, columnspan=2)

        self.o_label = tk.Label(root, text="O wins: 0", font=("Helvetica", 16))
        self.o_label.grid(row=3, column=1, columnspan=2)

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Resultado", f"¡{self.current_player} ganó!")
                if self.current_player == "X":
                    self.x_wins += 1
                    self.x_label.config(text=f"X wins: {self.x_wins}")
                else:
                    self.o_wins += 1
                    self.o_label.config(text=f"O wins: {self.o_wins}")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
