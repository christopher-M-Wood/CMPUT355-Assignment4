# Attributes
#   score
#   dimensions
#   available moves
#   comleted moves
#   list of possible boxes

class Board:
    # Initializer (takes number of rows and columns)
    def __init__(self, rows, cols):
        # TODO: Jared
        return

    # Create a queue of all available moves/lines that can be played on this board, given a particular number of rows and columns
    def generateMoves(self, r, c):
        # Should store each line on the board as a set (tuple) of coordinates in a queue
        # TODO: Ian
        return

    # Creates a list of Box objects (from box.py)
    def generateBoxes(self, rows, cols):
        # TODO: Jared
        return

    # Prints a text representation of the current board state for the command line
    def displayBoard(self):
        # TODO: Jared
        return

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
