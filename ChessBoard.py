from Piece import Piece
import copy


class ChessBoard(object):
    """
    A chessboard Object for this Tic-Tac-Toe game.
    """

    def __init__(self):
        """ Set up the chessboard.

        @param ChessBoard self: this ChessBoard
        @rtype: None
        """
        self.board = []
        self.SetUpChessBoard()

    def SetUpChessBoard(self):
        """ Set up the look of the chessboard.

        @rtype: None
        """
        # Create all the Piece objects on the chessboard.
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Piece(self.board, i, j))

        # Set up the four Pieces in the middle of the chessboard.
        self.SetUpPieces()

        # Update all the Piece objects on the chessboard with neighbours.
        for i_list in self.board:
            for piece in i_list:
                piece.UpdateNeighbours()

    def Draw(self):
        """ Draw this chessboard.

        @param ChessBoard self: this ChessBoard
        @rtype: None
        """
        # Set up the String representation of this chessboard.
        s = ""
        for i in range(len(self.board)):
            if i == 0:
                for k in range(17):
                    # If this is an even row:
                    if k == 0:
                        s += "\\"
                    elif k % 2 == 0:
                        s += str((k // 2) - 1)
                        # If this is the last column.
                        if k == 16:
                            s += "\n"
                    # If this is an odd row:
                    else:
                        s += "|"

                for k in range(17):
                    # If this is an even row:
                    if k % 2 == 0:
                        s += "-"
                        # If this is the last column.
                        if k == 16:
                            s += "\n"
                    # If this is an odd row:
                    else:
                        s += "+"

            # Draw out the row with all the Pieces.
            for j in range(len(self.board[i])):
                # If this is the last column.
                if j == 0:
                    s += str(i) + "|" + self.board[i][j].value + "|"
                elif j == len(self.board[i]) - 1:
                    s += self.board[i][j].value + "\n"
                else:
                    s += self.board[i][j].value + "|"
            # Draw out the
            if i < 7:
                for k in range(17):
                    # If this is an even row:
                    if k % 2 == 0:
                        s += "-"
                        # If this is the last column.
                        if k == 16:
                            s += "\n"
                    # If this is an odd row:
                    else:
                        s += "+"
        print(s)

    def MovesLeft(self, player):
        """ Return how many spots on the chessboard is left available.

        @param int player: the player this function is performed for
        @param ChessBoard self: this ChessBoard
        @rtype: list
        """
        moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].Check(player)[0]:
                    moves.append((i, j))
        return moves

    def SetUpPieces(self):
        """ Set up the four Pieces in the middle of the chessboard.

        @rtype: None
        """
        self.board[3][3].MakeMove(-1)
        self.board[4][4].MakeMove(-1)
        self.board[3][4].MakeMove(1)
        self.board[4][3].MakeMove(1)

    def MakeMove(self, row, col, player):
        """ Make the move of occupying a tile.

        @param ChessBoard self: this ChessBoard
        @param int row: the row of the tile
        @param int col: the column of the tile
        @param int player: either 1 or -1; 1 if this is player, -1 if this is computer
        @rtype: None
        """
        if self.board[row][col].Check(player)[0]:
            for direction in self.board[row][col].Check(player)[1]:
                self.board[row][col].ChangeValue(direction, player)
            self.board[row][col].MakeMove(player)

    def Copy(self):
        """ Returns a copy of this ChessBoard.

        @param ChessBoard self: this ChessBoard
        @rtype: ChessBoard
        """
        newChessBoard = ChessBoard()
        newChessBoard.board = copy.deepcopy(self.board)
        return newChessBoard

    def Count(self, player):
        """ Return the count of the pieces for the player.

        @param ChessBoard self: this ChessBoard
        @param int player: the player we want to count pieces for
        @rtype: the number of pieces there is for the player
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if player == 1 and self.board[i][j].value == "X":
                    # Corner positions are worth 10 points.
                    if (i == 0 and j == 0) or (i == 0 and j == 7) or (i == 7 and j == 0) or (i == 7 and j == 7):
                        count += 100
                    # Side positions are worth 5 points.
                    elif i == 0 or j == 0 or i == 7 or j == 7:
                        count += 15
                    else:
                        count += 1
                if player == -1 and self.board[i][j].value == "O":
                    # Corner positions are worth 10 points.
                    if (i == 0 and j == 0) or (i == 0 and j == 7) or (i == 7 and j == 0) or (i == 7 and j == 7):
                        count += 100
                    # Side positions are worth 5 points.
                    elif i == 0 or j == 0 or i == 7 or j == 7:
                        count += 15
                    else:
                        count += 1
        return count


if __name__ == "__main__":
    chessboard = ChessBoard()
    chessboard.Draw()
    print("X :")
    print(chessboard.MovesLeft(1))
    print(chessboard.Count(1))
    print("O :")
    print(chessboard.MovesLeft(-1))
    print(chessboard.Count(-1))

    print("\n")

    newChessBoard = chessboard.Copy()
    newChessBoard.MakeMove(2, 3, 1)
    print("Old: ")
    chessboard.Draw()
    print("New: ")
    newChessBoard.Draw()

    chessboard.MakeMove(2, 3, 1)
    chessboard.Draw()
    print("X :")
    print(chessboard.MovesLeft(1))
    print(chessboard.Count(1))
    print("O :")
    print(chessboard.MovesLeft(-1))
    print(chessboard.Count(-1))

    chessboard.MakeMove(2, 2, -1)
    chessboard.Draw()
    print("X :")
    print(chessboard.MovesLeft(1))
    print(chessboard.Count(1))
    print("O :")
    print(chessboard.MovesLeft(-1))
    print(chessboard.Count(-1))
