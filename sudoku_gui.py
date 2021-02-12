import tkinter as tk
from tkinter import *
import sudoku

root = Tk()
root.title("Sudoku Solver")
root.resizable(width=False, height=False)
root.config(bg="black")

board = [[], [], [], [], [], [], [], [], []]
new_board = [[], [], [], [], [], [], [], [], []]


def method():
    for i in range(0, 9):
        for j in range(0, 9):
            if not board[i][j].get().isdigit():
                new_board[i].append(0)
            else:
                new_board[i].append(int(board[i][j].get()))
    sudoku.solve(new_board)
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j].delete(0, END)
            board[i][j].insert(0, new_board[i][j])
            board[i][j].config(state=DISABLED)

    solve_button.grid_forget()


def limit_one():
    for i in range(0, 9):
        for j in range(0, 9):
            if len(board[i][j].get()) > 1:
                board[i][j].delete(1, END)
    solve_button.after(100, limit_one)


def only_digits():
    for i in range(0, 9):
        for j in range(0, 9):
            if not board[i][j].get().isdigit():
                board[i][j].delete(0, END)
    solve_button.after(100, only_digits)


for i in range(0, 9):
    board[0].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[0][i].grid(column=i, row=0)
    if i <= 2:
        board[0][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")
    elif 2 < i <= 5:
        board[0][i].config(bg="purple", disabledbackground="purple", disabledforeground="black")
    elif 5 < i <= 8:
        board[0][i].config(bg="yellow", disabledbackground="yellow", disabledforeground="black")
for i in range(0, 9):
    board[1].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[1][i].grid(column=i, row=1)
    if i <= 2:
        board[1][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")
    elif 2 < i <= 5:
        board[1][i].config(bg="purple", disabledbackground="purple", disabledforeground="black")
    elif 5 < i <= 8:
        board[1][i].config(bg="yellow", disabledbackground="yellow", disabledforeground="black")
for i in range(0, 9):
    board[2].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[2][i].grid(column=i, row=2)
    if i <= 2:
        board[2][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")
    elif 2 < i <= 5:
        board[2][i].config(bg="purple", disabledbackground="purple", disabledforeground="black")
    elif 5 < i <= 8:
        board[2][i].config(bg="yellow", disabledbackground="yellow", disabledforeground="black")
for i in range(0, 9):
    board[3].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[3][i].grid(column=i, row=3)
    if i <= 2:
        board[3][i].config(bg="green", disabledbackground="green", disabledforeground="black")
    elif 2 < i <= 5:
        board[3][i].config(bg="white", disabledbackground="white", disabledforeground="black")
    elif 5 < i <= 8:
        board[3][i].config(bg="red", disabledbackground="red", disabledforeground="black")
for i in range(0, 9):
    board[4].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[4][i].grid(column=i, row=5)
    if i <= 2:
        board[4][i].config(bg="green", disabledbackground="green", disabledforeground="black")
    elif 2 < i <= 5:
        board[4][i].config(bg="white", disabledbackground="white", disabledforeground="black")
    elif 5 < i <= 8:
        board[4][i].config(bg="red", disabledbackground="red", disabledforeground="black")
for i in range(0, 9):
    board[5].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[5][i].grid(column=i, row=6)
    if i <= 2:
        board[5][i].config(bg="green", disabledbackground="green", disabledforeground="black")
    elif 2 < i <= 5:
        board[5][i].config(bg="white", disabledbackground="white", disabledforeground="black")
    elif 5 < i <= 8:
        board[5][i].config(bg="red", disabledbackground="red", disabledforeground="black")
for i in range(0, 9):
    board[6].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[6][i].grid(column=i, row=8)
    if i <= 2:
        board[6][i].config(bg="blue", disabledbackground="blue", disabledforeground="black")
    elif 2 < i <= 5:
        board[6][i].config(bg="orange", disabledbackground="orange", disabledforeground="black")
    elif 5 < i <= 8:
        board[6][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")
for i in range(0, 9):
    board[7].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[7][i].grid(column=i, row=9)
    if i <= 2:
        board[7][i].config(bg="blue", disabledbackground="blue", disabledforeground="black")
    elif 2 < i <= 5:
        board[7][i].config(bg="orange", disabledbackground="orange", disabledforeground="black")
    elif 5 < i <= 8:
        board[7][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")
for i in range(0, 9):
    board[8].append(Entry(root, width=2, font=("Helvetica", 40), justify=CENTER))
    board[8][i].grid(column=i, row=10)
    if i <= 2:
        board[8][i].config(bg="blue", disabledbackground="blue", disabledforeground="black")
    elif 2 < i <= 5:
        board[8][i].config(bg="orange", disabledbackground="orange", disabledforeground="black")
    elif 5 < i <= 8:
        board[8][i].config(bg="cyan", disabledbackground="cyan", disabledforeground="black")

solve_button = Button(root, text="Solve", height=3, width=7, command=method)
solve_button.grid(column=4, row=11)

limit_one()
only_digits()

root.mainloop()
