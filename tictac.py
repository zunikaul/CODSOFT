import math


board = [" " for _ in range(9)]


def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]           
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X, AI is O")
    print_board()

    while True:
       
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Spot already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter number from 1-9.")
            continue

        board[move] = "X"
        print_board()

        if check_winner("X"):
            print("Congratulations! You won")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins! Better luck next time ")
            break
        if is_draw():
            print("It's a draw")
            break

# Run the game
play_game()
