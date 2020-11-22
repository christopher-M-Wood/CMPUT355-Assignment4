# Search algorithm for Dots and Boxes
import board

import copy
import random

class Minimax:
    scores = {}

    # Swaps the lines of a box
    # type = 0: Swap top and bottom, type = 1: Swap left and right, type = 2: Swap top and left,
    # type = 3: Swap top and right, type = 4: Swap bottom and left, type = 5: Swap bottom and right
    def swapSides(self, box, swap_type=0):
        out = copy.deepcopy(box)
        if (swap_type == 0):
            temp = out.topline
            out.topline = out.bottomline
            out.bottomline = temp
            temp = out.top_done
            out.top_done = out.bottom_done
            out.bottom_done = temp
        elif (swap_type == 1):
            temp = out.leftline
            out.leftline = out.rightline
            out.rightline = temp
            temp = out.left_done
            out.left_done = out.right_done
            out.right_done = temp
        elif (swap_type == 2):
            temp = out.topline
            out.topline = out.leftline
            out.leftline = temp
            temp = out.top_done
            out.top_done = out.left_done
            out.left_done = temp
        elif (swap_type == 3):
            temp = out.topline
            out.topline = out.rightline
            out.rightline = temp
            temp = out.top_done
            out.top_done = out.right_done
            out.right_done = temp
        elif (swap_type == 4):
            temp = out.bottomline
            out.bottomline = out.leftline
            out.leftline = temp
            temp = out.bottom_done
            out.bottom_done = out.left_done
            out.left_done = temp
        elif (swap_type == 5):
            temp = out.bottomline
            out.bottomline = out.rightline
            out.rightline = temp
            temp = out.bottom_done
            out.bottom_done = out.right_done
            out.right_done = temp
        return out

    # Mirrors a list of boxes about the axis
    # axis = 0: Mirror about horizontal axis, axis = 1: Mirror about vertical axis, axis = 3: Mirror about y=-x
    def mirror(self, board, axis=0):
        box_list = board.box_list
        if (axis == 0):
            board.box_list = [self.swapSides(box_list[6],0), self.swapSides(box_list[7],0), self.swapSides(box_list[8],0),
                                self.swapSides(box_list[3],0), self.swapSides(box_list[4],0), self.swapSides(box_list[5],0),
                                self.swapSides(box_list[0],0), self.swapSides(box_list[1],0), self.swapSides(box_list[2],0)]
        elif (axis == 1):
            board.box_list = [self.swapSides(box_list[2],1), self.swapSides(box_list[1],1), self.swapSides(box_list[0],1),
                                self.swapSides(box_list[5],1), self.swapSides(box_list[4],1), self.swapSides(box_list[3],1),
                                self.swapSides(box_list[8],1), self.swapSides(box_list[7],1), self.swapSides(box_list[6],1)]
        elif (axis == 2):
            board.box_list = [self.swapSides(self.swapSides(box_list[0],2),5), self.swapSides(self.swapSides(box_list[3],2),5), self.swapSides(self.swapSides(box_list[6],2),5),
                                self.swapSides(self.swapSides(box_list[1],2),5), self.swapSides(self.swapSides(box_list[4],2),5), self.swapSides(self.swapSides(box_list[7],2),5),
                                self.swapSides(self.swapSides(box_list[2],2),5), self.swapSides(self.swapSides(box_list[5],2),5), self.swapSides(self.swapSides(box_list[8],2),5)]
        return board
            
    def genIsos(self, o_board):
        if not (o_board.dimensions[0] == 3 and o_board.dimensions[1] == 3):
            return None
        r_isos = []
        # Basic boxes (0,1,2,3,4,5,6,7,8)
        r_isos.append(o_board)
        # Mirrored about the horizontal axis (6,7,8,3,4,5,0,1,2)
        r_isos.append(self.mirror(o_board))
        # Mirrored about the vertical axis (2,1,0,5,4,3,8,7,6)
        r_isos.append(self.mirror(o_board, 1))
        # Mirrored about the vertical and then horizontal axes (8,7,6,5,4,3,2,1,0)
        r_isos.append(self.mirror(self.mirror(o_board, 1)))
        # Mirrored about the line y=-x (0,3,6,1,4,7,2,5,8)
        r_isos.append(self.mirror(o_board, 2))
        # Mirrored about the vertical axis and then about the line y=-x (2,5,8,1,4,7,0,3,6)
        r_isos.append(self.mirror(self.mirror(o_board, 1), 2))
        # Mirrored about the horizontal and vertical axes and then about the line y=-x (8,5,2,7,4,1,6,3,0)
        r_isos.append(self.mirror(self.mirror(self.mirror(o_board), 1), 2))
        # Mirrored about the horizontal axis and then about the line y=-x (6,3,0,7,4,1,8,5,2)
        r_isos.append(self.mirror(self.mirror(self.mirror(o_board), 2)))
        return r_isos

    def getScore(self, board):
        if (len(self.scores) < 1):
            return (None,None)
        isos = self.genIsos(board)
        for key in self.scores:
            if not (isos == None):
                for i in isos:
                    if (key.equals(i)):
                        if (key.player == board.player):
                            return (i,self.scores[key])
                        else:
                            return (None,None)
            else:
                if (key.equals(board)):
                    if (key.player == board.player):
                        return (board,self.scores[key])
                    else:
                        return (None,None)
        return (None,None)

    def miniMax(self, board, depth, alpha=-1000, beta=1000):
        board.generateChildren()
        if ((board.moves_remaining == 0) or (board.depth >= depth)):
            self.scores.update({board: board.game_score})
            return board.game_score
        (b_iso, out) = self.getScore(board)
        if (b_iso == None):
            b_iso = board
        # IF IT'S MAX TURN
        if (board.player == "Player 2"):
            if (out == None):
                out = alpha
            best_score = out # WC for MAX 
            for child in board.children:
                result = self.miniMax(child, depth, alpha, beta)
                if (result > best_score):
                    best_score = result # Found a better best move
                if (best_score > alpha):
                    alpha = best_score
                # Check for pruning
                if alpha >= beta:
                    #break
                    self.scores.update({b_iso: alpha})
                    return alpha #Break early
            board.value = best_score
            self.scores.update({b_iso: best_score})
            return best_score
            
        # IF IT'S MIN TURN
        elif (board.player == "Player 1"):
            if (out == None):
                out = beta
            best_score = out # WC FOR MIN
            for child in board.children:
                result = self.miniMax(child, depth, alpha, beta)
                if (result < best_score):
                    best_score = result # Opponent has found a better worse move
                if best_score < beta:
                    beta = best_score
                # Check for pruning
                if beta <= alpha:
                    #break
                    self.scores.update({b_iso: beta})
                    return beta #Break early
            board.value = best_score
            self.scores.update({b_iso: best_score})
            return best_score

    def getMove(self, board, depth=3):
        board_copy = copy.deepcopy(board)
        # GENERATE SCORES
        best_score = self.miniMax(board_copy, depth, -1000, 1000)
        best = []
        # Iterate through children of current state to find best best move
        for child in board_copy.children:
            if child.value == best_score:
                best.append(child.move)
        if (len(best) > 0):
            return random.choice(best)
        else:
            # If there was no best move, set to last child's value
            return random.choice(board_copy.available_moves)
