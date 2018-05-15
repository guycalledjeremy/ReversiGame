from sys import maxsize
from ChessBoard import ChessBoard


##======================================================================================================================
## Tree Builder
class Node(object):

    def __init__(self, depth, player, chessboard, value=0):
        """  A Node for the decision making of the computer.

         @param int depth: the current depth in this Node
         @param int player: either 1 or -1; 1 if this is player, -1 if this is computer
         @param ChessBoard chessboard: the ChessBoard this Node is performing on
         @param int value: the value of this move for the player or the computer
         @rtype: None
         """
        self.depth = depth
        self.player = player
        self.value = value
        self.chessboard = chessboard
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        """ Add all possible moves on the chessboard as children for this Node.

        @rtype: None
        """
        if self.depth >= 1:
            moves_left = self.chessboard.MovesLeft(self.player)
            # The number of possible moves is based on how many legal moves are left on the chessboard.
            for i in range(len(moves_left)):
                # The row of this possible move position.
                i_row = moves_left[i][0]
                # The column of this possible move position.
                i_col = moves_left[i][1]
                newChessBoard = self.chessboard.Copy()
                # Make a new move at the tile (i_row, i_col).
                newChessBoard.MakeMove(i_row, i_col, self.player)
                # If the depth is 1, then we want to evaluate its children which are the leaves of this decision tree;
                # or if there is no move left on the chessboard.
                if self.depth == 1 or len(newChessBoard.MovesLeft(self.player)) == 1:
                    self.children.append(Node(self.depth - 1,
                                              -self.player,
                                              newChessBoard,
                                              self.RealVal(newChessBoard)))
                # In other cases the value should be initiated as 0.
                else:
                    self.children.append(Node(self.depth - 1,
                                              -self.player,
                                              newChessBoard))

    def RealVal(self, chessboard):
        """ Return the value for this leaf Node.

        @param ChessBoard chessboard: the chessboard to be evaluated
        @rtype: int
        """
        return chessboard.Count(-1) - chessboard.Count(1)

    ##==================================================================================================================
    ## Alpha-Beta Prunning Algorithm

    def AlphaBeta(self, alpha, beta):
        """ The Alpha-Beta Prunning algorithm sets the self.value to be the the minimum value of its children when
        player is -1, and the maximum value when player is 1. In addition, it decides whether or not to traverse
        through the whole tree based on self.value, alpha and beta.

        @rtype: None
        """
        # Check if it is a leaf Node or if this Node will result in one side winning the game.
        if self.depth == 0 or len(self.chessboard.MovesLeft(self.player)) == 0:
            # Pass because the base case is handled in RealVal when setting up the Node tree.
            pass
        else:
            # Initialise the value for this Node.
            ABValue = maxsize * self.player

            for child in self.children:
                # Recursive function call.
                child.AlphaBeta(alpha, beta)

                # Check if this Node is a maximiser Node.
                if self.player == -1:
                    if ABValue <= child.value:
                        ABValue = child.value
                    # Check if we should go for the next child Node.
                    if beta <= ABValue:
                        self.value = ABValue
                        break
                    else:
                        alpha = max(ABValue, alpha)
                # Check if this Node is a minimiser Node.
                else:
                    if child.value <= ABValue:
                        ABValue = child.value
                    # Check if we should go for the next child Node.
                    if ABValue <= alpha:
                        self.value = ABValue
                        break
                    else:
                        beta = min(beta, ABValue)

                self.value = ABValue


if __name__ == "__main__":
    chessboard = ChessBoard()
    chessboard.Draw()
    chessboard.MakeMove(2, 3, 1)
    chessboard.Draw()
    decisionTree = Node(5, -1, chessboard)
    decisionTree.AlphaBeta(-maxsize, maxsize)
    for child in decisionTree.children:
        print(child.value)
        child.chessboard.Draw()
        print('\n')
