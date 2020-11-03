# Attributes
#   self.board = Board(x,y) from board.py
#   self.depth = depth of search

import sys

import board
import box

class DotsAndBoxes:
    # Initializer
    def __init__(self,x,y):
        # TODO: Chris
        self.board = board.Board(x,y)

    # The game loop
    def play(self):
        # TODO: Chris
        self.board.displayBoard()
        while (len(self.board.available_moves) > 0):
            self.playerTurn(self)
        self.getWinner(self)

    # Handles user input
    def playerTurn(self):
        # TODO: Chris
        move = input ('Enter your move ([Pt1] [Pt2]): ')
        moves = move.split(' ')
        while (len(moves) != 2):
            move = input('Please enter moves according to the form [x1,y1] [x2,y2]: ')
            moves = move.split(' ')
        self.board.connectDots([moves[0], moves[1]], 'Human')
        self.board.displayBoard()

    # Determine who won, print out final state and relevant data
    def getWinner(self):
        # TODO: Victor
        return

# Main running order of the code
if __name__ == '__main__':
    # TODO: Chris
    if (len(sys.argv) < 3):
        print('Please call this file as \'python3 dotsAndBoxes.py [X] [Y]')
    else:
        dab = DotsAndBoxes(sys.argv[1], sys.argv[2])
        dab.play()
