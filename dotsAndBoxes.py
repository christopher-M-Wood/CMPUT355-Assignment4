"""
    A class used to handle the game-play for Dots and Boxes
    
    Attributes
    -------
    self.board: Board 
        A Board object with specified dimensions

    self.depth: int
        Specifies how deeply to search the game-tree, as chosen by the player

    self.gametype: int
        Specifies how to play (0 = P v AI, 1 = P v P, 2 = AI v AI)

    self.turn: int
        Tracks which player is playing on the current state.

    Methods
    -------
    play(self):
        The main game loop.

    takeInput(self, inputString)
        Handles the user's help menu selection and prints appropriately
    
    playerTurn(self, player)
        Handles game-play when it is the player's turn 
    
    computerTurn(self, player)
        Handles game-play when it is the computer's (AI) turn
    
    randomMove(self)
        Returns a random move from all available moves

    getWinner(self)
        Determines winner based on score and prints a message

    takeMenuInput(inputString, inputType)
        Handles given user input

"""

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
    def __init__(self,x,y,gametype,depth,turn):
        self.board = board.Board(x+1,y+1)
        self.depth = depth
        self.gametype = gametype
        self.turn = turn

    # The game loop
    def play(self):
        while True:
            self.board.displayBoard(gametype)
            while (len(self.board.available_moves) > 0):
                # gametype 0 is AI v AI; gametype 1 is P v AI; gametype 2 is P v P
                if self.gametype == 0 or self.turn == 2:
                    start = time.time()
                    self.computerTurn("Player 1") # AI P1
                    end = time.time()
                    print("Player 1 (AI) took " + str(end - start) + " seconds!\n")
                else:
                    self.playerTurn("Player 1")
            
                if (len(self.board.available_moves) > 0):
                    if self.gametype == 2 or self.turn == 2:
                        self.playerTurn("Player 2") # Human is P2
                    else:
                        start = time.time()
                        self.computerTurn("Player 2") # AI is P2
                        end = time.time()
                        print("Player 2 (AI) took " + str(end - start) + " seconds!\n")

            self.getWinner()
            temp = self.takeInput('Would you like to play again? (Y/N): ')
            if (temp == 'Y' or temp == 'y'):
                self.board = board.Board(self.board.dimensions[0], self.board.dimensions[1]) 
            else:
                break

    # Controls input related to the Help menu
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

    # Handles a player turn
    def playerTurn(self, player):
        # Play again is a trinary value (0,1,2) based on the output key from board.py connectDots
        self.board.mode = "Human"
        play_again = 0

        while (play_again != 1 and len(self.board.available_moves) > 0):
            if (play_again == 2):
                if self.board.completed == 2: # Player has another turn
                    print(player + ' completed 2 boxes. Please play another move.')
                else:
                    print(player + ' completed a box. Please play another move.')
           
            # Input handling
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

            # Get the player's move
            self.board.player = player
            play_again = self.board.connectDots((l, k), player)

            self.board.displayBoard(gametype)

    # Handles an AI turn
    def computerTurn(self, player):
        # Play again is a trinary value (0,1,2) based on the output key from board.py connectDots
        self.board.mode = "AI"
        play_again = 0

        while (play_again != 1 and len(self.board.available_moves) > 0):
            if (play_again == 2): # Player has another turn
                if self.board.completed == 2:
                    print(player + ' (AI) completed 2 boxes. They play another move.')
                else:
                    print(player + ' (AI) completed a box. They play another move.')
            print("\n"+player+' (AI) is making a move...')

            # Get the player's move
            move = None 
            self.board.player = player
            # For a Random Player
            if self.depth == 0:
                move = self.randomMove() 
            # For a Minimax Player
            else:
                algorithm = miniMax.Minimax()
                move = algorithm.getMove(self.board, self.depth, player)

            # Printing the current score
            l = move[0]
            k = move[1]
            print(player+ ' (AI) is playing ' + str(l) + ' ' + str(k) + '.')

            play_again = self.board.connectDots((l,k), player)

            self.board.displayBoard(gametype)

    # Returns a random move from all available choices
    def randomMove(self):
        return random.choice(self.board.available_moves)
            
    # Determine who won, print out final state and relevant data
    def getWinner(self):
        # TODO: Victor
        player1 = self.board.score[0]
        player2 = self.board.score[1]
        
        # Player 1 score > Player 2 score
        if (player1 > player2): 
            print("Player 1 Wins!\n\nPlayer 1 Score:",player1,"\nPlayer 2 Score:",player2,"\n")
            
        # Player 1 score < Player 2 score     
        elif (player1 < player2):
            print("Player 2 Wins!\n\nPlayer 1 Score:",player1,"\nPlayer 2 Score:",player2,"\n")
            
        # Player 1 score = Player 2 score
        elif (player1 == player2):
            print("Tie!\n\nPlayer 1 Score:",player1,"\nPlayer 2 Score:",player2,"\n")

#processes various input for starting menu          
def takeMenuInput(inputString, inputType): 
    min_range = 0 #gametype
    max_range = 3

    if inputType == "diff":
        max_range = 6

    elif inputType == "turn":
        min_range = 1

    out = "invalid"
    while (out == "invalid"):
        try:
            val = int(input(inputString))
            for i in range(min_range,max_range):
                if val == i:
                    return val
            break
        except ValueError:
            return out
    return out
        
        
# Main running order of the code
if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print('Please call this file as \'python3 dotsAndBoxes.py [X] [Y]\'')
        exit()
    try:
        test1 = int(sys.argv[1])
        test2 = int(sys.argv[2])
    except:
        print('Please call this file as \'python3 dotsAndBoxes.py [X] [Y]\'')
    else:
        depth = 4 # Default sim AI difficulty
        turn = None # Null value by default
        while True:
            gametype = takeMenuInput("\nWelcome to Dots and Boxes!\n\nIn this game, you may place one line on your turn. If you are the one to\ncomplete a box on the grid, you get a point and may move again.\nThat's all there is to it, really!\n\nEnter 1 if you would like to play against the AI.\nEnter 2 if you are playing against a friend.\nEnter 0 if you would like to see an AI vs. AI simulation.\n", "gametype")
            while gametype == "invalid":
                gametype = takeMenuInput('Please enter a number from 0-2: ', "gametype")
            break
        if gametype == 0: # AI simulation
            while True:    
                depth = takeMenuInput("\nWhat difficulty would you like the AI to play at?\nPlease specify as a number from 0-5: ", "diff")
                while depth == "invalid":
                    depth = takeMenuInput("Please enter a number from 0-5: ", "diff") 
                break            
        if gametype == 1: # Player versus AI
            while True:    
                depth = takeMenuInput("\nHow difficult of an AI would you like to play against?\nPlease specify as a number from 0-5: ", "diff")
                while depth == "invalid":
                    depth = takeMenuInput("Please enter a number from 0-5: ", "diff") 
                break            
            while True:    
                turn = takeMenuInput("\nWould you like to go first or second?\nPlease enter 1 or 2: ", "turn")
                while turn == "invalid":
                    turn = takeMenuInput("Please enter either 1 or 2: ", "turn") 
                break                
        print(info)
        dab = DotsAndBoxes(int(sys.argv[1]), int(sys.argv[2]), gametype, depth, turn)
        dab.play()

