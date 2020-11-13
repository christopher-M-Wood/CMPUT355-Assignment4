# Search algorithm for Dots and Boxes
import copy

class Minimax:

    def miniMax(self, board, depth, alpha=-1000, beta=1000):
        board.generateChildren()
        if ((board.depth >= depth) or len(board.children) == 0):
            return board.game_score

        # Do we want to allow option for player to select who goes first?
        # Max = whoever goes first?

        # IF IT'S MAX TURN
        if (board.player == "Player 1"):
            #alpha = -1000 # WC for MAX 
            for child in board.children:
                result = self.miniMax(child, depth - 1, alpha, beta)
                if (result > alpha):
                    alpha = result # Found a better best move
                # Check for pruning
                if alpha >= beta:
                    return alpha #Break early
            board.value = alpha
            return alpha 
            
        # IF IT'S MIN TURN
        elif (board.player == "Player 2"):
            #beta = 1000 # WC FOR MIN
            for child in board.children:
                result = self.miniMax(child, depth - 1, alpha, beta)
                if (result < beta):
                    beta = result # Opponent has found a better worse move
                # Check for pruning
                if beta <= alpha:
                    return beta #Break early
            board.value = beta
            return beta

    def getMove(self, board, depth=10):
        board = copy.deepcopy(board)

        # GENERATE SCORES
        best_move = self.miniMax(board, depth, -1000, 1000)
        #move = board.children[0]
        # Iterate through children of current state to find best best move
        for child in board.children:
            if child.game_score == best_move:
                move = child.move
                return move
            # If here was no best move, set to last child's value
            move = child.move 
        return move
