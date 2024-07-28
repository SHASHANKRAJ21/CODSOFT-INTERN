import numpy as np

# Initialize the board
def initialize_board():
    return np.zeros((3, 3), dtype=int)

# Display the board
def print_board(board):
    symbols = {0: ' ', 1: 'X', 2: 'O'}
    for row in board:
        print(" | ".join([symbols[x] for x in row]))
        print("-" * 5)

# Check if a player has won
def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check for a draw
def check_draw(board):
    return not any(0 in row for row in board)

# Make a move on the board
def make_move(board, row, col, player):
    if board[row][col] == 0:
        board[row][col] = player
        return True
    return False

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
    if check_win(board, 1):
        return -1
    if check_win(board, 2):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the AI
def best_move(board):
    best_val = float('-inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                move_val = minimax(board, 0, False)
                board[i][j] = 0
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

# Main game loop
def play_game():
    board = initialize_board()
    human_player = 1
    ai_player = 2
    current_player = human_player

    while True:
        print_board(board)
        if current_player == human_player:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if make_move(board, row, col, human_player):
                if check_win(board, human_player):
                    print("Human wins!")
                    break
                current_player = ai_player
            else:
                print("Invalid move. Try again.")
        else:
            row, col = best_move(board)
            make_move(board, row, col, ai_player)
            if check_win(board, ai_player):
                print("AI wins!")
                break
            current_player = human_player

        if check_draw(board):
            print("It's a draw!")
            break

play_game()

