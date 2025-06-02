import tkinter as tk
from tkinter import messagebox

def on_button_click(row, col):
    global current_player

    if game[row][col] == '':
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player)
        check_winner()
        current_player = "O" if current_player == "X" else "X"

def check_winner():
    combos = (game[0], game[1], game[2], [game[i][0] for i in range(3)],
              [game[i][1] for i in range(3)], [game[i][2] for i in range(3)],
              [game[i][i] for i in range(3)], [game[i][2 - i] for i in range(3)])
    for combo in combos:
        if combo[0] == combo[1] == combo[2] != '':
            announce_winner(combo[0])
    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        announce_winner("Draw")

def announce_winner(player):
    messagebox.showinfo("Game Over", "It's a draw!" if player == "Draw" else f"Player {player} wins!")
    reset_game()

def reset_game():
    global game, current_player
    game = [['' for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in buttons:
        for button in row:
            button.configure(text='')

# main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# create buttons using standard tkinter
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text='', width=10, height=5, font=('Helvetica', 20),
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

game = [['' for _ in range(3)] for _ in range(3)]
current_player = "X"

window.mainloop()
