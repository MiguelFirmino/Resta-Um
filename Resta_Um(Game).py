import tkinter as tk
import Resta_Um_Logic as game_logic

root = tk.Tk()

WIDTH = 600
HEIGHT = 600
BUTTON_WIDTH = 72
BUTTON_HEIGHT = 72
PIECE_IMAGE = tk.PhotoImage(file='restaumpiece.png')
HOLE_IMAGE = tk.PhotoImage(file='restaumhole.png')

canvas = tk.Canvas(root, width= WIDTH, height= HEIGHT, bg='#c5d1ed')
canvas.pack()

frame = tk.Frame(canvas, bg= '#e5e8ec')
frame.place(relx= 0.5, rely= 0.05, relwidth= 0.9, relheight= 0.9, anchor= 'n')
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

board_parts = [*game_logic.board]
game_buttons = []

for board_part in board_parts:
    if board_part.is_button:
        screen_button = tk.Button(frame, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='white', command=lambda x= board_part: click_button(x))
        screen_button.grid(row=board_part.row, column=board_part.column)
        board_part.button = screen_button
        game_buttons.append(board_part)
    else:
        empty_part = tk.Frame(frame, width= BUTTON_WIDTH, height= BUTTON_HEIGHT, bg='#e5e8ec')
        empty_part.grid(row=board_part.row, column=board_part.column)


selected_button = None
def click_button(clicked_button):
    global selected_button
    if not any(button.is_selected for button in game_buttons):
        clicked_button.is_selected = True
        selected_button = clicked_button
        selected_button.button.configure(relief= 'sunken')
    else:
        game_logic.check_moves(selected_button, clicked_button)
        selected_button.button.configure(relief= 'raised')
        for button in game_buttons:
            button.is_selected = False
        update_board()

def update_board():
    global game_buttons
    for button in game_buttons:
        if button.has_piece:
            button.button.configure(image= PIECE_IMAGE)
        else:
            button.button.configure(image= HOLE_IMAGE)

update_board()
root.mainloop()