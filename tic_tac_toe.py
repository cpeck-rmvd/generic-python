import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.buttons = [[tk.Button() for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, width=5, height=2, command=lambda i=i, j=j: self.play(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.player = "X"
        self.root.mainloop()

    def play(self, i, j):
        button = self.buttons[i][j]
        if button["text"] == "":
            button["text"] = self.player
            self.check_win()
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.end_game(self.buttons[i][0]["text"])
                return
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.end_game(self.buttons[0][i]["text"])
                return

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.end_game(self.buttons[0][0]["text"])
            return
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.end_game(self.buttons[0][2]["text"])
            return
        draw = True
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    draw = False
                    break
            if not draw:
                break
            if draw:
                self.end_game("draw")

    def end_game(self, winner):
        if winner == "draw":
            messagebox.showinfo("Game Over", "Its a draw!")
        else:
            messagebox.showinfo("Game Over", winner + " wins!")
        self.root.destroy()

TicTacToe()
