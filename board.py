import box
import copy

class Board:
    # Attributes
    #   score
    #   dimensions
    #   available moves
    #   completed moves
    #   list of possible boxes
    
    # Initializer (takesnumber of rows and columns)
    def __init__(self, x, y):
        # Convert string input to integer
        self.col = int(x)
        self.row = int(y)

        self.completed = 0
        self.box_list = []
        self.score = [0,0] # Format: [p1,p2]
        self.game_score = 0
        self.dimensions = [self.col, self.row]
        
        self.available_moves = self.generateMoves(self.col,self.row)
        self.completed_moves = []
        self.possible_boxes = self.generateBoxes(self.col,self.row)

        self.mode = None # "Human" or "AI"
        self.player = None # "Player 1" or "Player 2"
        self.move = None # Move that resulted in this state
        self.depth = 0 # Starting depth
        self.moves_remaining = len(self.available_moves)
        self.children = [] # Children states of the board
        self.value = None # Value from miniMax algorithm

    # Compare self to another board
    # If the two boards have the same number of boxes and for each box, the state of all lines match, they are equal, else not equal
    def equals(self, comp):
        if not (len(self.box_list) == len(comp.box_list)):
            return False
        for i in range(len(self.box_list)):
            a = self.box_list[i]
            b = comp.box_list[i]
            if not (a.top_done == b.top_done and a.left_done == b.left_done and a.right_done == b.right_done and a.bottom_done == b.bottom_done):
                return False
        return True
    
    # Create a queue of all available moves/lines that can be played on this board, given a particular number of rows and columns
    def generateMoves(self, c, r):
        available = []
        for i in range(0,c):
            for j in range(0,r-1):
                available.append(((i,j),(i, j+1)))
        for i in range(0,c-1):
            for j in range(0,r):
                available.append(((i,j),(i+1, j)))

        return available
        # Should store each line on the board as a set (tuple) of coordinates in a queue
        # NOTE from Jared: I coded the text representation to use ((x,y),(x,y)), so a tuple of tuples
        # TODO: Ian 

    # Creates a list of Box objects (from box.py)
    def generateBoxes(self, cols, rows):
        for i in range(cols-1):
            for j in range(rows-1):
                a_box = box.Box(i,j)
                self.box_list.append(a_box)
        return self.box_list

    # Prints a text representation of the current board state for the command line
    def displayBoard(self, gametype):
        for i in range(0,self.dimensions[1]-1):
            horiz_row = ""
            for j in range(0,self.dimensions[0]):
                cell_width = "."
                if ((j,i),(j+1,i)) in self.completed_moves or ((j+1,i),(j,i)) in self.completed_moves:
                #note that for all these if statements, j and i are flipped because it has to print row by row
                #but I wanted to preserve the (x,y) coordinate format
                    cell_width += "_____"
                else:
                    cell_width += "     "
                horiz_row += cell_width
            print(horiz_row)
            vert_row = ""
            for j in range(0,self.dimensions[0]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves or ((j,i+1),(j,i)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "     "
                vert_row += cell_width
            print(vert_row)
            box_marker_row = ""
            for j in range(0,self.dimensions[0]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves or ((j,i+1),(j,i)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "  "
                if j != self.dimensions[0]-1:
                    box_found = False
                    for box in self.possible_boxes:
                        if box.top_left[0] == j and box.top_left[1] == i and box.complete:
                            if (gametype == 1 and box.filled_by[0] == 1):
                                cell_width = "| AI" + "  "
                            else:
                                cell_width += str(box.filled_by[1]) + "  "
                            box_found = True
                    if box_found == False:
                        cell_width += "   "
                else:
                    cell_width += "   "
                box_marker_row += cell_width
            print(box_marker_row)
            print(vert_row)
        horiz_row = ""
        for j in range(0,self.dimensions[0]):
            cell_width = "."
            if ((j,self.dimensions[1]-1),(j+1,self.dimensions[1]-1)) in self.completed_moves or ((j+1,self.dimensions[1]-1),(j,self.dimensions[1]-1)) in self.completed_moves:
                cell_width += "_____"
            else:
                cell_width += "     "
            horiz_row += cell_width
        print(horiz_row)


    # Check self.available_moves for the coordinates given in the parameters
    # If the coordinates are in self.possible_moves then:
    #   - Remove the coordinates from self.possible_moves
    #   - Add the coordinates to self.completed_moves
    #   - Check our list of boxes (call checkBoxes()) to determine if we have an completed boxes with this new line
    #   - RETURN: 0-Not a valid move, 1-Valid move, 2-Completed a box (Chris)
    def connectDots(self, coordinates, player):
        # TODO: Ian
      
        if coordinates in self.available_moves:
        	self.available_moves.remove(coordinates)
        	self.completed_moves.append((coordinates[0],coordinates[1]))
        elif ((coordinates[1],coordinates[0])) in self.available_moves:
            self.available_moves.remove((coordinates[1],coordinates[0]))
            self.completed_moves.append((coordinates[1],coordinates[0]))
            # Flip coordinates back to normal
            coordinates = (coordinates[1],coordinates[0])
        else: 
            print('Error. Coordinates not valid')
            return 0

        if (self.checkBoxes(coordinates, player) == True):
            return 2
        else:
            return 1

    # Checks the list of boxes to see if the coordinates for the newly-added line from connectDots() completes a box
    # Increment score for player who completed the box
    # Change self.owner in Box object (from box.py) to player's identity
    # Return True if box is completed
    def checkBoxes(self, coordinates, player):
        # TODO: Victor
        
        #By default
        box = False
        self.completed = 0

        # For box in box_list
        for b in self.box_list:
            # For each line of the box four edges
            for line in b.lines:
                # Check if coordinates match an edge
                if coordinates == line:
                    b.connect(coordinates) #Call connect() function in box.py
                    if b.complete == True: #Check if box is completed after the call
                        
                        self.completed += 1

                        box = True         #Set default to True
                        if b.filled_by == None:
                            # Player 1 or Player 2
                            if player == "Player 1":
                                self.score[0] += 1    #Increment score
                                self.game_score += 1 
                                if self.mode == "AI":
                                    b.filled_by = (1,1)
                                else:
                                    b.filled_by = (0,1)
                                break
                            elif player == "Player 2":
                                self.score[1] += 1    #Increment score 
                                self.game_score = 1
                                if self.mode == "AI":
                                    b.filled_by = (1,2)
                                else:
                                    b.filled_by = (0,2)
                                break
            
        return box

    def generateChildren(self):
        for move in self.available_moves:
            # Create board object for child
            child = Board(self.row, self.col)

            #Initialize child's values
            child.box_list = copy.deepcopy(self.box_list)
            child.score = copy.deepcopy(self.score)
            child.game_score = copy.deepcopy(self.game_score)
            child.available_moves = copy.deepcopy(self.available_moves)
            child.completed_moves = copy.deepcopy(self.completed_moves)
            child.possible_boxes = copy.deepcopy(self.possible_boxes)
            
            if (self.player == "Player 1"):
                child.player = "Player 2"
            elif (self.player == "Player 2"):
                child.player = "Player 1"

            child.move = move
            child.depth = self.depth + 1
            child.moves_remaining = len(child.available_moves)
            child.children = []

            # Make the move on this child's board
            box = child.connectDots(move, child.player)
            
            if (box == 2):
                child.player = self.player

            # Add this updated board state to current state's children states
            self.children.append(child)
    
