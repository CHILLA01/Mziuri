board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True


# Printing the board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


# Take player input
def playerInput(board):
    global currentPlayer
    while True:
        try:
            if currentPlayer == "X":
                inp = int(input(f"Enter a number (1-9) \033[1;34m Player (X) \033[0;0m: "))
            else:
                inp = int(input(f"Enter a number (1-9) \033[1;31m Player (O) \033[0;0m: "))

            if 1 <= inp <= 9 and board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
                break
            else:
                print(f"Invalid input. Try again!")
                printBoard(board)
        except ValueError:
            print("Please enter a valid number between 1 and 9.")


# Check for win
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            winner = board[i]
            return True
    return False


def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            return True
    return False


def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[4]
        return True
    return False


def checkTie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


def checkWin():
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        return True
    return False


# Switch the player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"


# Game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin():
        gameRunning = False
    checkTie(board)
    if gameRunning:
        switchPlayer()
