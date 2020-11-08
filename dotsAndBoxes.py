# Attributes
#   self.board = Board(x,y) from board.py
#   self.depth = depth of search

import sys
import board
import box
from ast import literal_eval as make_tuple

class DotsAndBoxes:
    # Initializer
    def __init__(self,x,y):
        self.board = board.Board(x,y)

    # The game loop
    def play(self):
        self.board.displayBoard()
        
        while (len(self.board.available_moves) > 0):
            self.playerTurn("player1")
            self.playerTurn("player2")  #To be replaced with the AI
        
        self.getWinner()

    # Handles user input
    def playerTurn(self, player):

        # TODO: If Box is completed, current player continues
        # Victor -> I think we can return True/False in connectDots 
        #           to determine if current player continues
        play_again = True
        while (play_again):
            play_again = False
            move = input (player + ' enter your move ([Point1] [Point2]): ')
            moves = move.split(' ')
            while (len(moves) != 2):
                move = input('Please enter moves according to the form [x1,y1] [x2,y2]: ')
                moves = move.split(' ')
            l = make_tuple(moves[0])
            k = make_tuple(moves[1])

            play_again = self.board.connectDots((l, k), player)
            self.board.displayBoard()


    # Determine who won, print out final state and relevant data
    def getWinner(self):
        # TODO: Victor
        player1 = self.board.score[0]
        player2 = self.board.score[1]
        
        # Player 1 score > Player 2 score
        if (player1 > player2): 
            print("Player 1 Wins! --> ","Player 1 Score:",player1,"Player 2 Score:",player2)
            
        # Player 1 score < Player 2 score     
        elif (player1 < player2):
            print("Player 2 Wins! --> ","Player 1 Score:",player1,"Player 2 Score:",player2)
            
        # Player 1 score = Player 2 score
        elif (player1 == player2):
            print("Tie! --> ","Player 1 Score:",player1,"Player 2 Score:",player2)
            

# Main running order of the code
if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print('Please call this file as \'python3 dotsAndBoxes.py [X] [Y]')
    else:
        dab = DotsAndBoxes(sys.argv[1], sys.argv[2])
        dab.play()
