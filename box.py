# # Box is a data structure for representing a box on the game board
# --> Maintains Coordinates for a box's line (Top, Left, Bottom, Right)
# --> Tracks if a box's top, left, bottom, and right line are filled
# --> Tracks which player completed this box
# -->  Tracks if the box is complete (all sides filled)

class Box:
    def __init__(self, x, y):
        # x,y are coordinates for the for top left corner

        # Tracking if box is complete and which player completed it
        self.complete  = False 
        self.filled_by = None # tuple, first value is 0 for human and 1 for AI, second value is player

        # Tracks if a line is filled
        self.top_done    = False
        self.left_done   = False
        self.bottom_done = False
        self.right_done  = False

        #Top-Left coordinate represented as tuple
        self.top_left = (x,y)

        # Coordinates for box based on TL-corner coordinate
        self.coordinates = [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]

        # Coordinates (as tuple) for each box's line
        self.topline    = (self.coordinates[0], self.coordinates[1])
        self.leftline   = (self.coordinates[0], self.coordinates[2])
        self.bottomline = (self.coordinates[2], self.coordinates[3])
        self.rightline  = (self.coordinates[1], self.coordinates[3])
        
        # Array with all four lines' coordinates
        self.lines = [self.topline, self.leftline, self.rightline, self.bottomline]

    def connect(self, coordinates):
            # Check if given coordinates form a line of the current box.
            # - Coordinates is a tuple of a pair of tuples ((x1,y1),(x2,y2)) representing a line
            # - Returns a Bool True or False if a successful connection is made

        dots_connected = False # Boolean to return if coordinates connect as a line for this box
        if coordinates in self.lines:
            if   (coordinates == self.topline)    and (self.top_done == False):
                self.top_done  = True
                dots_connected = True
                
            elif (coordinates == self.leftline)   and (self.left_done == False):
                self.left_done = True
                dots_connected = True

            elif (coordinates == self.bottomline) and (self.bottom_done == False):
                self.bottom_done = True
                dots_connected   = True

            elif (coordinates == self.rightline)  and (self.right_done == False):
                self.right_done = True
                dots_connected  = True

        # Check if box is complete
        if self.top_done and self.left_done and self.bottom_done and self.right_done:
            self.complete = True

        return dots_connected
