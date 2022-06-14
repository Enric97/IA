from enum import Enum

boards = []
DEFAULT_BOARD = [[0,0,0],[0,0,0],[0,0,0]]
EMPTY = 0
O = 'O'
S = 'S'

class Player:
    O = 0
    S = 1

class BoardState:
    def __init__(self, board, pointsO, pointsS):
        self.children = []
        self.board = board
        self.pointsO = pointsO
        self.pointsS = pointsS

    def __str__(self):
        return str(self.board+" Points O: "+self.pointsO+" Points S: "+self.pointsS)

    def __repr__(self):
        return str(self.board+" Points O: "+self.pointsO+" Points S: "+self.pointsS)

def explore_tree(board_state, current_player):
    board_state.children = possible_children(board_state, current_player)
    current_player = change_player(current_player)
    for child in board_state.children:
        child = explore_tree(child, current_player)
    return board_state

def possible_children(board_state, current_player):
    children = []
    i = 0
    j = 0
    for line in board_state.board:
        j = 0
        for column in line:
            if is_empty(board_state.board[i][j]):
                new_board = move_current_player(board_state.board, i, j, current_player)
                children.append(new_board)
            j += 1
        i += 1        

    return children
            

def is_empty(box):
    return box == EMPTY

def move_current_player(board, i, j, current_player):
    board[i][j] = current_player
    return board

def change_player(current_player):
    if current_player == Player.O:
        return Player.S  
    else:
        return Player.O

def print_all(board_state):
    print(board_state.board)
    for child in board_state.children:
        print_all(child)

root = explore_tree(BoardState(DEFAULT_BOARD, 0, 0), Player.O)
print_all(root)