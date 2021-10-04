#Caroline Araujo and Isaiah Kolendo
#PA 4
import itertools
import copy
from datetime import datetime
startTime = 0
endTime = 0

def readBoard():
    board = []
    counter = 0
    with open("sudoku.txt", "r") as filestream:
        for line in filestream:
            liner = []
            currentline = line.split(",")
            for i in currentline:
                if i != '\n':
                    liner.append(i)
                    counter += 1
            board.append(liner)
    return board
def initializeBlanks(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ' ':
                board[i][j] = {'1','2','3','4','5','6','7','8','9'}
    return board

def solver(board):
    global startTime,endTime
    #check if we have any empty spaces left
    emptyFound = False
    for i in range(0,9):
        for j in range(0,9):
            if len(board[i][j]) > 1:
                emptyFound = True
                x = i
                y = j
                break
    if emptyFound == False:
        return True  #solution found --- go back on recursion
#now we check all the possible moves against the possible moves for a square and recurse on any valid move
    temp = board[x][y]                  #stores the list of all the valid moves for this square
    for i in range(1,10):
        val = str(i)
        if checkMove(board, x, y, val):#check if the move is valid
            board[x][y] = val          #if it is assign the spot that value
            copyBoard = copy.deepcopy(board)
            if solver(copyBoard):          #recurse with the new board, will only return true if the board s completly filled
                endTime = datetime.now()
                printBoard(board)
                totalTime = (endTime - startTime).total_seconds()
                print("Time to solve: ", totalTime)
                return#board           #filled valid board is returned
            else:
                temp.remove(val)
        else:
            temp.remove(val)
    board[x][y] = temp        #if a solution is not found reassign the spot to the previous value
    return

def checkMove(board,x,y,val):
    if checkRowsandColumns(board,x,y,val) and checkSquare(board,x,y,val):
        return True
    return False

def checkRowsandColumns(board,x,y,val): #check if chosen value is in row and column
    toReturn = True
    for i in range(0,9):
        if board[x][i] == val:
            toReturn = False
    for i in range(0,9):
        if board[i][y] == val:
            toReturn = False
    return toReturn

def checkSquare(board,x,y,val): #check if chosen value is in square
    toReturn = True
    x,y = getXY(x,y)
    tx =x
    ty = y
    possibleVals =[0,1,2]
    for i in possibleVals:
        for j in possibleVals:
            x = tx +i
            y = ty + j
            if board[x][y] == val:
                toReturn = False

    return toReturn
def getXY(x,y):
    x = int(x/3) * 3
    y = int(y/3) * 3
    return x,y


def printBoard(board):
    print("-------------------------------------")
    board = enumerate(board)
    for i, j in board:
        print(("|" + " {}   {}   {} | {}   {}   {} | {}   {}   {} |").format(*[y if y != 0 else " " for y in j]))
        if i == 8:
            print("-------------------------------------")
        elif i % 3 == 2:
            print("|" + "---+---+---+---+---+---+---+---+" + "---|")
        else:
            print("|" + "   +   +   +   +   +   +   +   +" + "   |")

def main():
    global startTime
    board = readBoard() #read board from text file
    print("Initial board:")
    printBoard(board)  #print initial board
    board = initializeBlanks(board)  #initialize blanks to {'1','2','3','4','5','6','7','8','9'}
    print("Solved board:")
    startTime = datetime.now()
    solver(board) 

if __name__ == '__main__':
    main()
