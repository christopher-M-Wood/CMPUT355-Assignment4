# Attributes
#   self.board = Board(x,y) from board.py
#   self.depth = depth of search

import sys
import random
import time

import board
import box
import miniMax

info = 'CONTROLS\n--------\nh,help\t : Prints this help guide\ni,input\t : Prints the proper format for inputing a move\nm,moves\t : Prints the available moves\nq,quit\t : Prints the current winner and then exits the program\ns,score\t : Prints the current score'
input_format = 'Moves are to be formatted as point pairs such that \'(x1,y1) (x2,y2)\''

class DotsAndBoxes:
    # Initializer
    def __init__(self,x,y,depth):
        self.board = board.Board(x+1,y+1)
        self.depth = depth

    # The game loop
    def play(self):
        while True:
            self.board.displayBoard()
            while (len(self.board.available_moves) > 0):
                self.playerTurn("Player 1")
                # Second Human Player
                # self.playerTurn("Player 2")
                
                # AI Player
                start = time.time()
                self.computerTurn()
                end = time.time()
                print("AI took " + str(end - start) + " seconds!")

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
        self.board.mode = "AI"
        play_again = 0
        while (play_again != 1 and len(self.board.available_moves) > 0):
            if (play_again == 2):
                print('The AI completed ' + str(self.board.completed) + ' boxes. They play another move.')
            print('The AI is making a move...')
            
            # For a Random Player
            # move = self.randomMove()

            # For a Minimax Player
            self.board.player = 'Player 2'
            algorithm = miniMax.Minimax()
            move = algorithm.getMove(self.board, self.depth)
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
            
#processes input for strength of AI            
def takeDiffInput(inputString):
    diffvalues = [1,2,3,4,5,6]    
    out = False
    while (out == False):
        try:
            val = int(input(inputString))
            for i in diffvalues:
                if val == i:
                    return val
            break
        except ValueError:
            return out
    return out
        
        
# Main running order of the code
if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print('Please call this file as \'python3 dotsAndBoxes.py [X] [Y]')
    else:
        gametype = None
        gametypevalues = [0,1,2]
        #for i in range(1,24):
            #depthvalues.append(i)
        #while True:
            #try:
                #gametype = int(input("Welcome to Dots and Boxes!\n\nIn this game, you may place one line per turn. If you are the one to\ncomplete a box on the grid, you get a point and may move again.\nThat's all there is to it, really!\n\nEnter 1 if you would like to play against the AI.\nEnter 2 if you are playing against a friend.\nEnter 0 if you would like to see an AI vs. AI simulation."))
                #q,quit         : Prints the current winner and then exits the program
                #while (len(moves) != 2):
                    #move = self.takeInput('Please enter moves according to the form \'(x1,y1) (x2,y2)\': ')
                #break
            #except ValueError:
                #print("Error. Please try again.")
        while True:    
            depth = takeDiffInput("How difficult of an AI would you like to play against?\nPlease specify as a number from 1-6: ")
            while depth == False:
                depth = takeDiffInput("Please enter a number from 1-6: ")  
            break            
        print(info)
        dab = DotsAndBoxes(int(sys.argv[1]), int(sys.argv[2]), depth)
        dab.play()

