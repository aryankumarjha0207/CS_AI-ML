import math

# Board representation
def create_board():
    return [' '] * 9

def print_board(board):
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---+---+---")
    print()

def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]             # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_terminal(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or not get_available_moves(board)

def evaluate(board):
    if check_winner(board, 'X'):   # AI
        return 10
    elif check_winner(board, 'O'): # Human
        return -10
    return 0  # Draw

# ---- Alpha-Beta Pruning ----
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if is_terminal(board):
        return evaluate(board)

    if is_maximizing:  # AI's turn (X)
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = alpha_beta(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:       # Beta cutoff
                break               # Prune remaining branches
        return max_eval

    else:              # Human's turn (O)
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = alpha_beta(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:       # Alpha cutoff
                break               # Prune remaining branches
        return min_eval

def best_move(board):
    best_val = -math.inf
    best_pos = -1
    print("  [AI thinking... evaluating moves]")
    for move in get_available_moves(board):
        board[move] = 'X'
        move_val = alpha_beta(board, 0, -math.inf, math.inf, False)
        board[move] = ' '
        print(f"  Move {move} → score: {move_val}")
        if move_val > best_val:
            best_val = move_val
            best_pos = move
    print(f"  AI picks position {best_pos}\n")
    return best_pos

# ---- Main Game Loop ----
def play():
    board = create_board()
    print("=== Tic-Tac-Toe with Alpha-Beta Pruning ===")
    print("You are O, AI is X")
    print("Board positions:")
    print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")

    # Randomly decide who goes first (or just let human go first)
    human_turn = True

    while not is_terminal(board):
        print_board(board)

        if human_turn:
            moves = get_available_moves(board)
            print(f"Available positions: {moves}")
            while True:
                try:
                    pos = int(input("Your move (0-8): "))
                    if pos in moves:
                        break
                    print("Invalid! Choose from available positions.")
                except ValueError:
                    print("Enter a number!")
            board[pos] = 'O'
        else:
            print("AI is making its move...")
            pos = best_move(board)
            board[pos] = 'X'

        human_turn = not human_turn

    print_board(board)

    if check_winner(board, 'X'):
        print("AI wins! (You tried your best)")
    elif check_winner(board, 'O'):
        print("You win! (The AI must be broken lol)")
    else:
        print("It's a draw! (AI never loses, but you held it off)")

if __name__ == "__main__":
    play()
