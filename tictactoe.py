"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in board:
        for col in row:
            if col == X:
                xCount += 1
            elif col == O:
                oCount += 1
    
    if xCount + oCount == 9:
        return None
    elif xCount > oCount:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]== EMPTY:
                acts.add((i, j))
    
    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid move") 
    else:
        copyBoard = copy.deepcopy(board)
        copyBoard[action[0]][action[1]] = player(board)

    return copyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Horizontal
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
                return board[i][0]
    #Vertical
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    #Diagonally
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X or board[0][0] == O:
            return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X or board[0][2] == O:
            return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) == None):
        for row in board:
            for col in row:
                if col == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win == X:
            return 1
        elif win == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        res = []
        for action in actions(board):
            res.append((minValue(result(board, action)), action))
            
        res = sorted(res, key=lambda x: x[0], reverse = True)
        return res[0][1]
    
    else:
        res = []
        for action in actions(board):
            res.append((maxValue(result(board, action)), action))
        
        res = sorted(res, key=lambda x: x[0])
        return res[0][1]


def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for act in actions(board):
        v = min(v, maxValue(result(board, act)))

    return v

def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    for act in actions(board):
        v = max(v, minValue(result(board, act)))

    return v