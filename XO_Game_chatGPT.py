import tkinter as tk
import random

# Constants
BG_COLOR = "#ffffff"
BTN_COLOR = "#f0f8ff"
WIN_COLOR = "#a0e7e5"
TIE_COLOR = "#ffc9de"
FONT = ("Arial", 24, "bold")

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toc Almadrasa")
root.geometry("500x700")
root.configure(bg=BG_COLOR)
root.grid_columnconfigure(tuple(range(9)), weight=1)

# Score variables
your_score, comp_score = tk.IntVar(value=0), tk.IntVar(value=0)

# Labels
score_label = tk.Label(root, font=FONT, bg=BG_COLOR)
score_label.grid(row=0, column=0, columnspan=9, pady=(30, 10), sticky="n")
result_label = tk.Label(root, font=FONT, bg=BG_COLOR, fg="black")
result_label.grid(row=1, column=0, columnspan=9, pady=10)

# Buttons grid
buttons = []

update_score = lambda: score_label.config(text=f"You: {your_score.get()}   Computer: {comp_score.get()}")

reset_buttons = lambda: [btn.config(text="", state="normal", bg=BTN_COLOR) for row in buttons for btn in row] or result_label.config(text="")

def check_winner():
    board = [[btn["text"] for btn in row] for row in buttons]
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]: return board[i][0], [(i, j) for j in range(3)]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]: return board[0][i], [(j, i) for j in range(3)]
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]: return board[0][0], [(i, i) for i in range(3)]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]: return board[0][2], [(0, 2), (1, 1), (2, 0)]
    if all(cell != "" for row in board for cell in row): return "Tie", [(i, j) for i in range(3) for j in range(3)]
    return None, []

def handle_winner(winner, pos):
    color = WIN_COLOR if winner in ["X", "O"] else TIE_COLOR
    result_label.config(text=f"{winner} wins!" if winner != "Tie" else "Tie, No Winner!", fg="green" if winner=="X" else "red" if winner=="O" else "black")
    [buttons[i][j].config(bg=color) for i, j in pos]
    [btn.config(state="disabled") for row in buttons for btn in row]
    if winner == "X": your_score.set(your_score.get() + 1)
    elif winner == "O": comp_score.set(comp_score.get() + 1)
    update_score()

def comp_move():
    empty = [btn for row in buttons for btn in row if btn["text"] == ""]
    if empty:
        choice = random.choice(empty)
        choice.config(text="O", state="disabled")
        winner, pos = check_winner()
        if winner: handle_winner(winner, pos)

def on_click(btn):
    if btn["text"] == "":
        btn.config(text="X", state="disabled")
        winner, pos = check_winner()
        if winner: handle_winner(winner, pos)
        else: root.after(300, comp_move)

def create_grid():
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2, bg=BTN_COLOR)
            btn.grid(row=i + 3, column=j + 3, padx=5, pady=5)
            btn.config(command=lambda b=btn: on_click(b))
            row.append(btn)
        buttons.append(row)

def restart_game():
    reset_buttons()

# Create game grid and restart button
create_grid()
tk.Button(root, text="Restart", font=("Arial", 20, "bold"), bg="#e6e6e6", command=restart_game).grid(row=2, column=3, columnspan=3, pady=10)

# Initialize score and run
update_score()
root.mainloop()
