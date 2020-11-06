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
        self.score = [0,0] #p1 then p2
        self.dimensions = [rows, cols]
        self.available_moves = self.generateMoves()
        self.completed_moves = []
        self.possible_boxes = self.generateBoxes()

    # Create a queue of all available moves/lines that can be played on this board, given a particular number of rows and columns
    def generateMoves(self, r, c):
        # Should store each line on the board as a set (tuple) of coordinates in a queue
        # TODO: Ian
        return

    # Creates a list of Box objects (from box.py)
    def generateBoxes(self, rows, cols):
        box_list = []
        for i in range(0,rows):
            for j in range(0,cols):
                box = Box(i, j)
                box_list.append(box)
        return box_list

    # Prints a text representation of the current board state for the command line
    '''def displayBoard(self):
        for i in self.generateMoves():
            if i in self.completed_moves:
                if i[0][0] == i[1][0]
        print(
        return
    i'll finish this up tomorrow - Jared
    '''

    # Check self.available_moves for the coordinates given in the parameters
    # If the coordinates are in self.available_moves then:
    #   - Remove the coordinates from self.available_moves
    #   - Add the coordinates to self.completed_moves
    #   - Check our list of boxes to determine if we have an completed boxes with this new line
    def connectDots(self, coordinates, player):
        # TODO: Ian
        return

    # Checks the list of boxes to see if the coordinates for the newly-added line completes a box
    # Increment score for player who completed the box
    # Change self.owner in Box object (from box.py) to player's identity
    def checkBoxes(self, coordinates, player):
        # TODO: Victor
        return
