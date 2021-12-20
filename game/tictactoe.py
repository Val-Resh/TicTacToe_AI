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
    countX, countO = 0,0
    for line in board:
        for value in line:
            if value == X:
                countX += 1
            if value == O:
                countO += 1
    return O if countX > countO else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                action_set.add((i,j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    new_board = copy.deepcopy(board)
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move!")
    else: 
        new_board[i][j] = player(board)
    return new_board

def winner_helper(board, player):
    """
    Helper function for the winner()
    """
    for i in range(len(board)):
        horizontal_bools = []
        vertical_bools = []
        for j in range(len(board)):
            horizontal_bools.append(board[i][j] == player)
            vertical_bools.append(board[j][i] == player)
        if len([x for x in horizontal_bools if x == True]) == 3:
            return player
        if len([x for x in vertical_bools if x == True]) == 3:
            return player
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
         return player
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
         return player
    return None
            
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winner_helper(board, X) == X:
        return X
    elif winner_helper(board, O) == O:
        return O
    else:
        None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if winner(board) or not actions(board) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = None
    alpha = -math.inf
    beta = math.inf
    if terminal(board):
        return move
    if player(board) == X:
        v = alpha
        for action in actions(board):
            x = min_value(result(board,action),v,beta)
            if x > v:
                v = x
                move = action
    else:
        v = beta
        for action in actions(board):
            x = max_value(result(board,action),alpha,v)
            if x < v:
                v = x
                move = action
    return move
                




def max_value(board, alpha, beta):
    """
    Helper function for minimax.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        x = min_value(result(board,action),alpha,beta)
        v = max(v, x)
        alpha = max(alpha, x)
        if beta <= alpha:
            break
    return v


def min_value(board, alpha, beta):
    """
    Helper function for minimax.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        x = max_value(result(board, action),alpha,beta)
        v = min(v,x)
        beta = min(beta, x)
        if beta <= alpha:
            break
    return v