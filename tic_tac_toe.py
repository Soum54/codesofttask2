import math

# Constants for representing the players and empty cells
EMPTY = '-'
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'

# Function to print the current board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if the board is full
def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, AI_PLAYER):
        return 1
    elif check_winner(board, HUMAN_PLAYER):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, AI_PLAYER):
        return 1
    elif check_winner(board, HUMAN_PLAYER):
        return -1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    eval = minimax(board, depth+1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, depth+1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to get the best move for the AI player
def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_PLAYER
                eval = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[EMPTY]*3 for _ in range(3)]
    print_board(board)

    while not is_full(board) and not check_winner(board, AI_PLAYER) and not check_winner(board, HUMAN_PLAYER):
        # Human player's turn
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] == EMPTY:
            board[row][col] = HUMAN_PLAYER
        else:
            print("Cell already occupied. Try again.")
            continue

        print_board(board)

        if check_winner(board, HUMAN_PLAYER):
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # AI player's turn
        print("AI's turn:")
        row, col = get_best_move(board)
        board[row][col] = AI_PLAYER
        print_board(board)

        if check_winner(board, AI_PLAYER):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
