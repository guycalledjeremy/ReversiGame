class Piece(object):
    """
    A Piece object representing a piece on the chessboard.
    """

    def __init__(self, chessboard, row, col):
        """ Initialise a new Piece object.

        @param list chessboard: the ChessBoard this Piece is on
        @param int row: the row which this Piece is on
        @param int col: the column which this Piece is on
        """
        self.value = " "
        self.row = row
        self.col = col
        self.chessboard = chessboard
        self.neighbours = []
        self.CreateNeighbours()

    def CreateNeighbours(self):
        """ Create a new list of neighbours with all 0's.

        @rtype: None
        """
        for i in range(8):
            self.neighbours.append(" ")

    def UpdateNeighbours(self):
        """ Update the list self.neighbours with the current chessboard.

        @rtype: None
        """
        # The count for which neighbour this loop is at.
        list_count = 0
        # list_count is 0 - 7, which represent all eight neighbours.
        for i in range(3):
            # r represents the relative row position.
            r = i - 1
            for j in range(3):
                # c represents the relative column position.
                c = j - 1
                # If this is not the point for this Piece
                if r == 0 and c == 0:
                    pass
                else:
                    if 0 <= self.row + r <= 7 and 0 <= self.col + c <= 7:
                            # and self.chessboard[self.row + r][self.col + c]:
                        # the neighbour's position = this Node's position + the relative position.
                        self.neighbours[list_count] = self.chessboard[self.row + r][self.col + c]
                    list_count += 1

    def Check(self, player):
        """ Return True iff this Piece is legal to be performed a move on.

        @param int player: the player this Check function is performed for
        @rtype: tuple
        """
        # This move will not be legal if this Piece is already occupied by a previous move.
        check = False
        directions = []
        if self.value != " ":
            return check, directions
        for i in range(8):
            if self.CheckNeighbour(i, player)[0] == 1:
                check = True
                directions.append(self.CheckNeighbour(i, player)[1])
        return check, directions

    def CheckNeighbour(self, direction, player):
        """ Return 1 iff this direction qualifies this Piece for a move.

        @param int player: the player this Check function is performed for
        @param int direction: the direction we want to check
        @rtype: tuple
        """
        # First convert player into the string representation of the Node value.
        if player == 1:
            player_value = "X"
        elif player == -1:
            player_value = "O"
        else:
            print("COMPUTER ERROR.")
            player_value = " "

        # If the neighbour in that direction is an empty place.
        if type(self.neighbours[direction]) == str:
            return 0, None
        elif self.neighbours[direction].value == " ":
            return 0, None
        # If the neighbour in that direction is not an empty place and and is a Piece of different value.
        elif self.neighbours[direction].value == player_value != self.value:
            if self.value != " ":
                return 1, direction
            else:
                return 0, None
        # If the neighbour in that direction is not an empty place and and is a Piece of same value.
        else:
            # Recursive call till self.neighbours is empty or a Piece of a different value.
            return self.neighbours[direction].CheckNeighbour(direction, player)

    def MakeMove(self, player):
        """ Change the value of this Piece for the player.

        @param int player: the player that wishes to make this move
        @rtype: None
        """
        if player == 1:
            self.value = "X"
        elif player == -1:
            self.value = "O"
        else:
            print("COMPUTER ERROR.")

    def ChangeValue(self, direction, player):
        """ Change the value for the player on the direction.

        @param int direction: the direction we want to change the value for
        @param int player: the player we want to change the value for
        @rtype: None
        """
        # First convert player into the string representation of the Node value.
        if player == 1:
            player_value = "X"
        elif player == -1:
            player_value = "O"
        else:
            print("COMPUTER ERROR.")
            player_value = " "

        # If the neighbour in that direction is an empty place.
        if type(self.neighbours[direction]) == str:
            pass
        elif self.neighbours[direction].value == " ":
            pass
        # If the neighbour in that direction is not an empty place and and is a Piece of different value.
        elif self.neighbours[direction].value == player_value != self.value and self.value != " ":
            pass
        # If the neighbour in that direction is not an empty place and and is a Piece of same value.
        else:
            # Recursive call till self.neighbours is empty or a Piece of a different value.
            self.neighbours[direction].ChangeValue(direction, player)
            self.neighbours[direction].value = player_value
