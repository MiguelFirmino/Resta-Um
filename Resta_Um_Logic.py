class BoardPart():
    def __init__(self, row, column, button, has_piece, is_selected, is_button):
        self.row = row
        self.column = column
        self.button = button
        self.has_piece = has_piece
        self.is_selected = is_selected
        self.is_button = is_button

board = [BoardPart(0, 0, None, None, None, False), BoardPart(0, 1, None, None, None, False), BoardPart(0, 2, None, True, False, True), BoardPart(0, 3, None, True, False, True), BoardPart(0, 4, None, True, False, True), BoardPart(0, 5, None, None, None, False), BoardPart(0, 6, None, None, None, False),
         BoardPart(1, 0, None, None, None, False), BoardPart(1, 1, None, None, None, False), BoardPart(1, 2, None, True, False, True), BoardPart(1, 3, None, True, False, True), BoardPart(1, 4, None, True, False, True), BoardPart(1, 5, None, None, None, False), BoardPart(1, 6, None, None, None, False),
         BoardPart(2, 0, None, True, False, True), BoardPart(2, 1, None, True, False, True), BoardPart(2, 2, None, True, False, True), BoardPart(2, 3, None, True, False, True), BoardPart(2, 4, None, True, False, True), BoardPart(2, 5, None, True, False, True), BoardPart(2, 6, None, True, False, True),
         BoardPart(3, 0, None, True, False, True), BoardPart(3, 1, None, True, False, True), BoardPart(3, 2, None, True, False, True), BoardPart(3, 3, None, False, False, True), BoardPart(3, 4, None, True, False, True), BoardPart(3, 5, None, True, False, True), BoardPart(3, 6, None, True, False, True),
         BoardPart(4, 0, None, True, False, True), BoardPart(4, 1, None, True, False, True), BoardPart(4, 2, None, True, False, True), BoardPart(4, 3, None, True, False, True), BoardPart(4, 4, None, True, False, True), BoardPart(4, 5, None, True, False, True), BoardPart(4, 6, None, True, False, True),
         BoardPart(5, 0, None, None, None, False), BoardPart(5, 1, None, None, None, False), BoardPart(5, 2, None, True, False, True), BoardPart(5, 3, None, True, False, True), BoardPart(5, 4, None, True, False, True), BoardPart(5, 5, None, None, None, False), BoardPart(5, 6, None, None, None, False),
         BoardPart(6, 0, None, None, None, False), BoardPart(6, 1, None, None, None, False), BoardPart(6, 2, None, True, False, True), BoardPart(6, 3, None, True, False, True), BoardPart(6, 4, None, True, False, True), BoardPart(6, 5, None, None, None, False), BoardPart(6, 6, None, None, None, False)]

def check_moves(selected_hole, target_hole):
    hole_in_between = None
    if selected_hole.has_piece and not target_hole.has_piece and selected_hole.row == target_hole.row:
        if selected_hole.column - target_hole.column == 2:
            for hole in board:
                if hole.column == selected_hole.column - 1 and hole.row == selected_hole.row:
                    hole_in_between = hole
                    if hole_in_between.has_piece:
                        move_piece(hole_in_between, selected_hole, target_hole)
                    break
        elif selected_hole.column - target_hole.column == -2:
            for hole in board:
                if hole.column == selected_hole.column + 1 and hole.row == selected_hole.row:
                    hole_in_between = hole
                    if hole_in_between.has_piece:
                        move_piece(hole_in_between, selected_hole, target_hole)
                    break

    elif selected_hole.has_piece and not target_hole.has_piece and selected_hole.column == target_hole.column:
        if selected_hole.row - target_hole.row == 2:
            for hole in board:
                if hole.row == selected_hole.row - 1 and hole.column == selected_hole.column:
                    hole_in_between = hole
                    if hole_in_between.has_piece:
                        move_piece(hole_in_between, selected_hole, target_hole)
                    break
        elif selected_hole.row - target_hole.row == -2:
            for hole in board:
                if hole.row == selected_hole.row + 1 and hole.column == selected_hole.column:
                    hole_in_between = hole
                    if hole_in_between.has_piece:
                        move_piece(hole_in_between, selected_hole= selected_hole, target_hole= target_hole)
                    break

def move_piece(hole_in_between, selected_hole, target_hole):
    hole_in_between.has_piece = False
    selected_hole.has_piece = False
    target_hole.has_piece = True