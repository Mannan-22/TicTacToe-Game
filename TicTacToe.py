import time

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True
firstPlayer = "X"

def printBoard(board):

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def resetBoard():
    global board, gameRunning
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    gameRunning = True


def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Oops! That spot is already taken.")

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    global gameRunning, firstPlayer, currentPlayer
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        firstPlayer = winner
        gameRunning = False

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def searchwinningOrBlockingMove(board, player):
    for i in range(9):
        if board[i] == "-":
            board[i] = player
            if checkHorizontle(board) or checkRow(board) or checkDiag(board):
                board[i] = "-"
                return i
            board[i] = "-"
    return None

def searchfirstAvailableMove(board):
    for i in range(9):
        if board[i] == "-":
            return i
    return None

def computer(board):
    if currentPlayer == "O":
        print("Computer's Turn:")
        time.sleep(0)

        move = searchwinningOrBlockingMove(board, "O")
        if move != None:
            board[move] = "O"
            switchPlayer()
            return

        move = searchwinningOrBlockingMove(board, "X")
        if move != None:
            board[move] = "O"
            switchPlayer()
            return

        move = searchfirstAvailableMove(board)
        if move != None:
            board[move] = "O"
            switchPlayer()
        else:
            print("The board is full! No move possible.")


while True:
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        if not gameRunning:
            break
        switchPlayer()
        computer(board)
        checkIfWin(board)

    resetBoard()
    print("\n--- Starting a new game! ---")
    print(f"{firstPlayer} will go first.")
    currentPlayer = firstPlayer

    if currentPlayer == "O":
        computer(board)
    else:
        playerInput(board)
    checkIfTie(board)






