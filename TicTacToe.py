board = [
    [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
]

Xturn = True

while True:

    print("\n\n\n\n\n\n\n\n")

    for row in board:
        print("".join(row))
        

    move = input()

    if move.lower() == "q":
        break



    if move == "1" and Xturn and board[0][1] == " ":
        board[0][1] = "X"
        Xturn = False
    elif move == "1" and Xturn == False and board[0][1] == " ":
        board[0][1] = "O"
        Xturn = True
        

    if move == "2" and Xturn and board[0][5] == " ":
        board[0][5] = "X"
        Xturn = False
    elif move == "2" and Xturn == False and board[0][5] == " ":
        board[0][5] = "O"
        Xturn = True

    if move == "3" and Xturn and board[0][9] == " ":
        board[0][9] = "X"
        Xturn = False
    elif move == "3" and Xturn == False and board[0][9] == " ":
        board[0][9] = "O"
        Xturn = True

    if move == "4" and Xturn and board[2][1] == " ":
        board[2][1] = "X"
        Xturn = False
    elif move == "4" and Xturn == False and board[2][1] == " ":
        board[2][1] = "O"
        Xturn = True

    if move == "5" and Xturn and board[2][5] == " ":
        board[2][5] = "X"
        Xturn = False
    elif move == "5" and Xturn == False and board[2][5] == " ":
        board[2][5] = "O"
        Xturn = True
    
    if move == "6" and Xturn and board[2][9] == " ":
        board[2][9] = "X"
        Xturn = False
    elif move == "6" and Xturn == False and board[2][9] == " ":
        board[2][9] = "O"
        Xturn = True
    
    if move == "7" and Xturn and board[4][1] == " ":
        board[4][1] = "X"
        Xturn = False
    elif move == "7" and Xturn == False and board[4][1] == " ":
        board[4][1] = "O"
        Xturn = True
    
    if move == "8" and Xturn and board[4][5] == " ":
        board[4][5] = "X"
        Xturn = False
    elif move == "8" and Xturn == False and board[4][5] == " ":
        board[4][5] = "O"
        Xturn = True
    
    if move == "9" and Xturn and board[4][9] == " ":
        board[4][9] = "X"
        Xturn = False
    elif move == "9" and Xturn == False and board[4][9] == " ":
        board[4][9] = "O"
        Xturn = True

    #horizontal win for X

    if board[0][1] == "X" and board[0][5] == "X" and board[0][9] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    if board[2][1] == "X" and board[2][5] == "X" and board[2][9] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    if board[4][1] == "X" and board[4][5] == "X" and board[4][9] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    
    #horizontal win for O

    if board[0][1] == "O" and board[0][5] == "O" and board[0][9] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
    if board[2][1] == "O" and board[2][5] == "O" and board[2][9] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
    if board[4][1] == "O" and board[4][5] == "O" and board[4][9] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break

    #vertical win for X

    if board[0][1] == "X" and board[2][1] == "X" and board[4][1] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    if board[0][5] == "X" and board[2][5] == "X" and board[4][5] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    if board[0][9] == "X" and board[2][9] == "X" and board[4][9] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break

    #vertical win for O

    if board[0][1] == "O" and board[2][1] == "O" and board[4][1] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
    if board[0][5] == "O" and board[2][5] == "O" and board[4][5] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
    if board[0][9] == "O" and board[2][9] == "O" and board[4][9] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break

    #diagonal win for X

    if board[0][1] == "X" and board[2][5] == "X" and board[4][9] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break
    if board[0][9] == "X" and board[2][5] == "X" and board[4][1] == "X":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("X won!")
        break

    #diagonal win for O

    if board[0][1] == "O" and board[2][5] == "O" and board[4][9] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
    if board[0][9] == "O" and board[2][5] == "O" and board[4][1] == "O":
        print("\n\n\n\n\n\n\n\n")
        for row in board:
            print("".join(row))
        print("O won!")
        break
