from sys import maxsize
from Node import Node
from ChessBoard import ChessBoard


##======================================================================================================================
## Game Implementation
def Check(chessboard):
    """ Check if the game ends and who won the game.

    @param ChessBoard chessboard: the chessboard this game is played on
    @rtype: int
    """
    # Check if this game ends by finishing all the spots.
    if len(thisChessboard.MovesLeft(1)) + len(thisChessboard.MovesLeft(-1)) == 0:
        print("*" * 60)
        if chessboard.Count(1) > chessboard.Count(-1):
            print("\tCongrats you won!!! =D")
        elif chessboard.Count(-1) < chessboard.Count(1):
            print("\tComputer won, maybe better luck next time... =(")
        else:
            print("\tSeems like it's a draw this time... New Game? =)")
        print("*" * 60)
        return 0
    else:
        return 1

if __name__ == "__main__":
    currPlayer = 1
    thisChessboard = ChessBoard()
    print("Welcome to the Reversi Game!!\n")
    print("How to play: place your piece to take over your opponent's pieces!")
    depth = int(input("Choose the depth for the computer(3, 4 or 5): \n"))

    while len(thisChessboard.MovesLeft(-1)) >= 0:
        print("This is the current board: \n")
        thisChessboard.Draw()
        print("These are all the legal moves: \n")
        print(thisChessboard.MovesLeft(1))
        print("Which tile would you want to play? \n")
        # Get the row and column for the play.
        row = int(input("Row (0 - 7): \n"))
        col = int(input("Column (0 - 7): \n"))
        while not thisChessboard.board[row][col].Check(currPlayer)[0]:
            print("\nSorry illegal spot, please choose from the given list: ")
            print(str(thisChessboard.MovesLeft(1)) + "\n")
            row = int(input("Row (0 - 7): \n"))
            col = int(input("Column (0 - 7): \n"))
        thisChessboard.MakeMove(row, col, currPlayer)
        # The depth of the decision node tree should be dynamically updated as how many moves are left.
        thisChessboard.Draw()

        currPlayer *= -1
        # Check if anyone wins the game.
        if Check(thisChessboard) != 0:
            decisionNode = Node(depth, currPlayer, thisChessboard)
            alpha = -maxsize
            beta = maxsize

            bestChoice = thisChessboard.board
            bestValue = maxsize * currPlayer
            # Get the best choice and the corresponding value using the Minmax algorithm.
            for i in range(len(decisionNode.children)):
                child = decisionNode.children[i]
                child.AlphaBeta(alpha, beta)

                if bestValue <= child.value:
                    bestValue = child.value
                    bestChoice = child.chessboard.board

            thisChessboard.board = bestChoice
            print("\nThe computer has moved. ")
            currPlayer *= -1

        Check(thisChessboard)
