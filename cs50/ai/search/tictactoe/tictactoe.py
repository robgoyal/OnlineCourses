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

    empties = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                empties += 1
    return X if empties % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                moves.add((row, col))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Create a copy of the board to avoid altering the original board
    board = copy.deepcopy(board)

    # Obtain key information
    move = player(board)
    row = action[0]
    col = action[1]

    # Check if action is valid
    if board[row][col] is not EMPTY:
        raise Exception
    board[row][col] = move
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    combinations = [
        # Winning row combinations
        {board[0][0], board[0][1], board[0][2]},
        {board[1][0], board[1][1], board[1][2]},
        {board[2][0], board[2][1], board[2][2]},
        # Winning column combinations
        {board[0][0], board[1][0], board[2][0]},
        {board[0][1], board[1][1], board[2][1]},
        {board[0][2], board[1][2], board[2][2]},
        # Winning diagonal combinations
        {board[0][0], board[1][1], board[2][2]},
        {board[2][0], board[1][1], board[0][2]}
    ]

    for combo in combinations:
        if len(combo) == 1:
            return combo.pop()
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    empties = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                empties += 1

    # True if there is a winner or no empty spaces
    return bool(winner(board)) or empties == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    utilities = {X: 1, O: -1}
    return utilities.get(winner(board), 0)


def minimizing_action(state):
    """
    Return the best value and action for the minimizing player (O)
    """

    # Initialize variable representing best action
    best_action = {"value": math.inf, "action": None}

    # Check if board is in a terminal state
    #   Return None for the action since this information isn't available in this frame
    if terminal(state):
        return {"value": utility(state), "action": None}

    for action in actions(state):
        move = maximizing_action(result(state, action))
        if move["value"] < best_action["value"]:
            # Update the best action and value if better move is found
            best_action["action"] = action
            best_action["value"] = move["value"]

    return best_action


def maximizing_action(state):
    """
    Return the best value and action for the maximizing player (X)
    """

    # Initialize variable representing best action
    best_action = {"value": -math.inf, "action": None}

    # Check if board is in a terminal state
    #   Return None for the action since this information isn't available in this frame
    if terminal(state):
        return {"value": utility(state), "action": None}

    for action in actions(state):
        move = minimizing_action(result(state, action))
        if move["value"] > best_action["value"]:

            # Update the best action and value if better move is found
            best_action["action"] = action
            best_action["value"] = move["value"]

    return best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        return maximizing_action(board)["action"]
    else:
        return minimizing_action(board)["action"]
