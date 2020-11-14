# Search algorithm for Dots and Boxes
import copy

class Minimax:

    def miniMax(self, board, depth, alpha=-1000, beta=1000):
        board.generateChildren()
        if ((board.moves_remaining == 0) or (board.depth >= depth)):
            return board.game_score

        # IF IT'S MAX TURN
        if (board.player == "Player 1"):
            best_score = -1000 # WC for MAX 
            for child in board.children:
                result = self.miniMax(child, depth - 1, alpha, beta)
                if (result > best_score):
                    best_score = result # Found a better best move
                if (best_score > alpha):
                    alpha = best_score
                # Check for pruning
                if alpha >= beta:
                    #break
                    return alpha #Break early
            board.value = best_score
            return best_score
            
        # IF IT'S MIN TURN
        elif (board.player == "Player 2"):
            best_score = 1000 # WC FOR MIN
            for child in board.children:
                result = self.miniMax(child, depth - 1, alpha, beta)
                if (result < best_score):
                    best_score = result # Opponent has found a better worse move
                if best_score < beta:
                    beta = best_score
                # Check for pruning
                if beta <= alpha:
                    #break
                    return beta #Break early
            board.value = best_score
            return best_score

    def getMove(self, board, depth=5):
        board = copy.deepcopy(board)

        # GENERATE SCORES
        best_score = self.miniMax(board, depth, -1000, 1000)
        # Iterate through children of current state to find best best move
        for child in board.children:
            if child.value == best_score:
                move = child.move
                return move
            # If there was no best move, set to last child's value
            move = child.move 
        return move
