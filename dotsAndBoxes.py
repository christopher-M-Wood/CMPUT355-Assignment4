# Attributes
#   self.board = Board(x,y) from board.py
#   self.depth = depth of search

import sys
import board
import box
from miniMax import Minimax
import random


info = 'CONTROLS\n--------\nh,help\t : Prints this help guide\ni,input\t : Prints the proper format for inputing a move\nm,moves\t : Prints the available moves\nq,quit\t : Prints the current winner and then exits the program\ns,score\t : Prints the current score'
input_format = 'Moves are to be formatted as point pairs such that \'(x1,y1) (x2,y2)\''

class DotsAndBoxes:
    # Initializer
    def __init__(self,x,y):
        self.board = board.Board(x+1,y+1)

    # The game loop
    def play(self):
        while True:
            self.board.displayBoard()
            while (len(self.board.available_moves) > 0):
                self.playerTurn("Player 1")
                # Second Human Player
                # self.playerTurn("Player 2")
                
                # AI Player
                self.computerTurn()

            self.getWinner()
            temp = self.takeInput('Would you like to play again? (Y/N): ')
            if (temp == 'Y' or temp == 'y'):
               self.board = board.Board(self.board.dimensions[0], self.board.dimensions[1]) 
            else:
                break

    def takeInput(self, inputString):
        out = ''
        while (out == ''):
            val = input(inputString)
            if (val == 'h' or val == 'help'):
                print(info)
            elif (val == 'i' or val == 'input'):
                print(input_format)
            elif (val == 'm' or val == 'moves'):
                print('Possible moves:')
                for i in self.board.available_moves:
                    print(str(i)[1:-1])
            elif (val == 'q' or val == 'quit'):
                self.getWinner()
                sys.exit()
            elif (val == 's' or val == 'score'):
                print('Current score -- Player1: ' + str(self.board.score[0]) + ' Player2: ' + str(self.board.score[1]))
            else:
                out = val
        return out

    # Takes a player turn
    def playerTurn(self, player):
        # Play again is a trinary value (0,1,2) based on the output key from board.py connectDots
        play_again = 0
        while (play_again != 1 and len(self.board.available_moves) > 0):
            if (play_again == 2):
                print(player + ' completed '+ str(self.board.completed) + ' boxes. Please play another move.')
            while True:
                try:        
                    move = self.takeInput(player + ' enter your move: ')
                    moves = move.split(' ')
                    while (len(moves) != 2):
                        move = self.takeInput('Please enter moves according to the form \'(x1,y1) (x2,y2)\': ')
                        moves = move.split(' ')
                    l = (int(moves[0][1]), int(moves[0][3]))
                    k = (int(moves[1][1]), int(moves[1][3]))
                    break
                except ValueError:
                    print("Error. Please try again.")
            self.board.player = 'Player 1'
            play_again = self.board.connectDots((l, k), player)
            self.board.displayBoard()

    def computerTurn(self):
        algorithm = Minimax()
        play_again = 0
        while (play_again != 1 and len(self.board.available_moves) > 0):
            if (play_again == 2):
                print('The AI completed ' + str(self.board.completed) + ' boxes. They play another move.')
            print('The AI is making a move...')
            # For a Random Player
            # move = self.randomMove()

            # For a Minimax Player
            self.board.player = 'Player 2'
            move = algorithm.getMove(self.board)
            l = move[0]
            k = move[1]
            print('The AI is playing ' + str(l) + ' ' + str(k) + '.')
            play_again = self.board.connectDots((l,k), 'Player 2')
            self.board.displayBoard()

    def randomMove(self):
        return random.choice(self.board.available_moves)
            
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
        print(info)
        dab = DotsAndBoxes(int(sys.argv[1]), int(sys.argv[2]))
        dab.play()
