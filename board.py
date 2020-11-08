import box

class Board:
    # Attributes
    #   score
    #   dimensions
    #   available moves
    #   completed moves
    #   list of possible boxes
    
    # Initializer (takesnumber of rows and columns)
    def __init__(self, rows, cols):
        # Convert string input to integer
        self.row = int(rows)
        self.col = int(cols)
        
        self.score = [0,0] # Format: [p1,p2]
        self.dimensions = [self.row, self.col]
        
        # TODO self.available_moves = self.generateMoves()
        
        self.completed_moves = []
        self.possible_boxes = self.generateBoxes(self.row,self.col)

    # Create a queue of all available moves/lines that can be played on this board, given a particular number of rows and columns
    def generateMoves(self, r, c):
        available = []
        for i in range(0,r):
            for j in range(0,c-1):
                available.append(((i,j),(i, j+1)))
        for i in range(0,r-1):
            for j in range(0,c):
                available.append(((i,j),(i+1, j)))

        return available
        # Should store each line on the board as a set (tuple) of coordinates in a queue
        # NOTE from Jared: I coded the text representation to use ((x,y),(x,y)), so a tuple of tuples
        # TODO: Ian

    # Creates a list of Box objects (from box.py)
    def generateBoxes(self, rows, cols):
        box_list = []
        for i in range(0,rows):
            for j in range(0,cols):
                self.box = box.Box(i, j)
                box_list.append(box)
        return box_list

    # Prints a text representation of the current board state for the command line
    def displayBoard(self):
        for i in range(0,self.dimensions[0]-1):
            horiz_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = "."
                if ((j,i),(j+1,i)) in self.completed_moves:
                    cell_width += "_____"
                else:
                    cell_width += "     "
                horiz_row += cell_width
            print(horiz_row)
            vert_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "     "
                vert_row += cell_width
            print(vert_row)
            box_marker_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "  "
                if j != self.dimensions[1]-1:
                    box_found = False
                    for box in self.possible_boxes:
                        if self.box.top_left[0] == j and self.box.top_left[1] == i and box.complete:
                            cell_width += str(box.filled_by)
                            box_found = True
                    if box_found == False:
                        cell_width += " "
                else:
                    cell_width += " "
                cell_width += "  "
                box_marker_row += cell_width
            print(box_marker_row)
            print(vert_row)
        horiz_row = ""
        for j in range(0,self.dimensions[1]):
            cell_width = "."
            if ((self.dimensions[0],j),(self.dimensions[0]+1,j)) in self.completed_moves:
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
    def connectDots(self, coordinates, player):
        # TODO: Ian
       	completeBox = False
        print(self.available_moves)
        if coordinates in self.available_moves:
        	self.available_moves.remove(coordinates)
        	self.completed_moves.append((coordinates[0],coordinates[1]))
        else: 
        	print("Error coordinates entered not valid")	
        
        if (checkBoxes(coordinates, player)):
        	completeBox = True;
        else:
        	completeBox = False;
        


        return completeBox
    # Checks the list of boxes to see if the coordinates for the newly-added line completes a box
    # Increment score for player who completed the box
    # Change self.owner in Box object (from box.py) to player's identity
    def checkBoxes(self, coordinates, player):
        # TODO: Victor
        
        #By default
        box = False
        #Get Player's current score
        player1 = self.board.score[0]
        player2 = self.board.score[1]
                
        # Check if the line is in any box's list
        if coordinates in self.possible_boxes:
            
            #Do something
            
           #If box is completed 
            box = True
            # Player 0 = AI, 1 = Person (from box.py)
            if player == "AI":
                player1 += 1
                box.filled_by = 0
            elif player == "Human":
                player2 += 1
                box.filled_by = 1
        
           
        return box