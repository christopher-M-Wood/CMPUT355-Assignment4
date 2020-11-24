# Search algorithm for Dots and Boxes
import board

import copy
import random

class Minimax:
    descendants = []

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
        b_list = copy.deepcopy(board.box_list)
        if (axis == 0):
            board.box_list = [self.swapSides(b_list[6],0), self.swapSides(b_list[7],0), self.swapSides(b_list[8],0),
                                self.swapSides(b_list[3],0), self.swapSides(b_list[4],0), self.swapSides(b_list[5],0),
                                self.swapSides(b_list[0],0), self.swapSides(b_list[1],0), self.swapSides(b_list[2],0)]
        elif (axis == 1):
            board.box_list = [self.swapSides(b_list[2],1), self.swapSides(b_list[1],1), self.swapSides(b_list[0],1),
                                self.swapSides(b_list[5],1), self.swapSides(b_list[4],1), self.swapSides(b_list[3],1),
                                self.swapSides(b_list[8],1), self.swapSides(b_list[7],1), self.swapSides(b_list[6],1)]
        elif (axis == 2):
            board.box_list = [self.swapSides(self.swapSides(b_list[0],2),5), self.swapSides(self.swapSides(b_list[3],2),5), self.swapSides(self.swapSides(b_list[6],2),5),
                                self.swapSides(self.swapSides(b_list[1],2),5), self.swapSides(self.swapSides(b_list[4],2),5), self.swapSides(self.swapSides(b_list[7],2),5),
                                self.swapSides(self.swapSides(b_list[2],2),5), self.swapSides(self.swapSides(b_list[5],2),5), self.swapSides(self.swapSides(b_list[8],2),5)]
        return board
            
    def genIsos(self, o_board):
        # Basic boxes (0,1,2,3,4,5,6,7,8)
        r_isos = [o_board]
        if (o_board.dimensions[0] == 4 and o_board.dimensions[1] == 4):
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

    def pruneDescendants(self, board):
        output = []
        board.generateChildren()
        return board.children
        #for child in board.children:
        #    e = False
        #    if (len(self.descendants) > 0):
        #        c_isos = self.genIsos(child)
        #        for exist in self.descendants:
        #            for c in c_isos:
        #                if (c.equals(exist)):
        #                    e = True
        #                    break
        #            if (e == True):
        #                break
        #    if (e == False):
        #        output.append(child)
        #        self.descendants.append(child)
        #return output

    def miniMax(self, board, depth, alpha=-1000, beta=1000):
        #checking = self.pruneDescendants(board)
        board.generateChildren()
        if ((board.moves_remaining == 0) or (depth <= 0)):
            if (board.game_score == None):
                return 0
            else:
                return board.game_score

        # IF IT'S MAX TURN
        if (board.player == "Player 2"):
            best_score = -1000 # WC for MAX 
            for child in board.children:
                result = self.miniMax(child, depth-1, alpha, beta)
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
        elif (board.player == "Player 1"):
            best_score = 1000 # WC FOR MIN
            for child in board.children:
                result = self.miniMax(child, depth-1, alpha, beta)
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

    def getMove(self, board, depth):
        board_copy = copy.deepcopy(board)
        # GENERATE SCORES
        score = self.miniMax(board_copy, depth, -1000, 1000)
        best = []
        print(score)
        # Iterate through children of current state to find best best move
        for child in board_copy.children:
            print(child.value)
            if child.value == score:
                best.append(child.move)
        print(best)
        if (len(best) > 1):
            return random.choice(best)
        elif (len(best) == 1):
            return best[0]
        else:
            # If there was no best move, set to last child's value
            return random.choice(board_copy.available_moves)

