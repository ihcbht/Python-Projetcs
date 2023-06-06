import random
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-",]

cp="X"
win=None
gamerun=True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# printboard(board)

def pinput(board):
    inp=int(input("Enter a number between 1-9 :"))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=cp
    else:
        print("Already filled")

def Horizontal(board):
    global win
    if board[0] == board[1] == board[2] and board[0] != "-":
        win = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        win = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        win = board[6]
        return True
    
def Vertical(board):
    global win
    if board[0] == board[3] == board[6] and board[0] != "-":
        win = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        win = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        win = board[3]
        return True

def Diagonal(board):
    global win
    if board[0] == board[4] == board[8] and board[0] != "-":
        win = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        win = board[2]
        return True
    
def tie(board):
    if "-" not in board:
        printboard(board)
        print("The game ends in a tie")
        gamerun=False


def checkWin(board):
    if Diagonal(board) or Horizontal(board) or Vertical(board):
        printboard(board)
        print(f"The winner is {win}")
        quit()
    

def switchp():
    global cp
    if cp == "X":
        cp = "O"
    else:
        cp = "X"

def automaticplayer(board):
    while cp == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchp()



while gamerun:
    printboard(board)
    pinput(board)
    checkWin(board)
    tie(board)
    switchp()
    automaticplayer(board)
    checkWin(board)
    tie(board)