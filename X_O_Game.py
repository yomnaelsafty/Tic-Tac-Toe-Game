import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toc Almadrasa")
root.geometry("450x700")
root.configure(bg="#f0f0f0")

your_score = tk.IntVar(value=0)
comp_score = tk.IntVar(value=0)

score_label = tk.Label(root, text=f"You: {your_score.get()}     Computer: {comp_score.get()}", font=("Arial", 24, "bold"),
    bg="#f0f0f0" )

score_label.grid(row=0, column=0, columnspan=9, pady=(30, 10), sticky="n")

result_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="black")
result_label.grid(row=1, column=0, columnspan=9, pady=10)




buttons = []

def check_winner():
    board =[]
    for row in buttons:
        board_row = []
        for btn in row:
             board_row.append(btn["text"])
        board.append(board_row)

    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0], [(i, 0), (i, 1), (i, 2)]
    
    for j in range(3):
        if board[0][j] != "" and board[0][j] == board[1][j] ==board[2][j]:
            return board[0][j], [(0, j), (1, j), (2, j)]
    
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0], [(0, 0), (1, 1), (2, 2)]

    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2], [(0, 2), (1, 1), (2, 0)]

    all_filled = all(btn["text"] != "" for row in buttons for btn in row)

    if all_filled:
        return "Tie", []

    return None, []

def handle_winner(winner, winning_positions):
    if winner == "X":
        your_score.set(your_score.get() + 1)
        result_label.config(text="X wins!", fg="black")
        color = "cyan"
    elif winner == "O":
        comp_score.set(comp_score.get() + 1)
        result_label.config(text="Computer wins!", fg="black")
        color = "cyan"
    elif winner == "Tie":
        result_label.config(text="Tie, No Winner!", fg="black")
        color = "red"
        winning_positions = [(i, j) for i in range(3) for j in range(3)]

    score_label.config(text=f"You: {your_score.get()}   Computer: {comp_score.get()}")

    for i, j in winning_positions:
          buttons[i][j].config(bg=color)

  
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")


def comp_move():
    empty_btn = []
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                empty_btn.append(btn)

    if empty_btn:
        comp_choice = random.choice(empty_btn) 
        comp_choice.config(text="O", state="disabled") 
        winner, pos = check_winner()
        if winner:
            handle_winner(winner, pos)
 



for row in range(3):
    button_row = []
    for col in range(3):
        btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2)
        btn.grid(row=row + 3, column=col + 3, padx=5, pady=5)

        def on_click(b=btn):
           if b["text"] == "":
              b.config(text="X", state="disabled")
              winner, pos = check_winner()
              if winner:
                  handle_winner(winner, pos)
              else:
                  root.after(500, comp_move)
        
        btn.config(command=on_click)
        button_row.append(btn)
    buttons.append(button_row)


def restart_game():

    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal", bg="SystemButtonFace")

    result_label.config(text="")

tk.Button(root, text="Restart", font=("Arial", 20, "bold"), bg="#d9d9d9", command=restart_game).grid(row=2, column=3, columnspan=3, pady=10, padx=10)

root.mainloop()
