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

        self.box_list = []
        self.score = [0,0] # Format: [p1,p2]
        self.dimensions = [self.row, self.col]
        
        self.available_moves = self.generateMoves(self.row,self.col)
        
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
        for i in range(0,rows):
            for j in range(0,cols):
                self.box = box.Box(i, j)
                self.box_list.append(self.box)
        return self.box_list

    # Prints a text representation of the current board state for the command line
    def displayBoard(self):
        for i in range(0,self.dimensions[0]-1):
            horiz_row = ""
            for j in range(0,self.dimensions[1]):
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
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves or ((j,i+1),(j,i)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "     "
                vert_row += cell_width
            print(vert_row)
            box_marker_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves or ((j,i+1),(j,i)) in self.completed_moves:
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
            if ((j,self.dimensions[0]-1),(j+1,self.dimensions[0]-1)) in self.completed_moves or ((j+1,self.dimensions[0]-1),(j,self.dimensions[0]-1)) in self.completed_moves:
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
                
        # For box in box_list, if coordinates in box.lines
        for b in self.box_list:
            if coordinates in b.lines:
                b.connect(coordinates) #Call connect() function in box.py
                if b.complete == True: #Check if box is completed after the call
                    box = True         #Set default to True
                    if b.filled_by == None:
                        # Player 0 = AI, 1 = Person (from box.py)
                        if player == "Player1":
                             self.score[0] += 1    #Increment score
                             b.filled_by = 0       #Set who completed the box
                             break
                        elif player == "Player2":
                             self.score[1] += 1    #Increment score 
                             b.filled_by = 1       #Set who completed the box
                             break
            else:
                break
        return box

