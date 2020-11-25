# Dots and Bots

A player for Dots and Boxes created for Assignment 4 of CMPUT 355, Fall 2020. 

## About Dots and Boxes

Dots and Boxes is a zero-sum game for two players that is easily played with pencil and paper. It is was invented by French mathematician Édouard Lucas who called it 'La pipopipette'. The game begins with a grid of dots, and players take turns connecting two dots with a single line. If a player successfully completes the fourth side of a box, the player gets another turn. The player continues to play another turn as long as they complete a box. Otherwise, the turn switches to their opponent. The game ends when there are no more dots left to connect; the winner is the player with the most points (1 point earned per box that is completed). 

## About This Program

This program includes four files:

- board.py
- box.py
- dotsAndBoxes.py
- miniMax.py

This is a terminal-based game. To begin, the user should input: ***python3 dotsAndBoxes.py 3 3*** into their terminal. The program works with grids of all sizes, although we began with 3x3 in mind, and larger grids result in increasingly slower 'moves' by the AI as it attempts to search larger game trees. The AI is implemented using the Mini Max algorithm with Alpha-Beta pruning. Additional functions for future versions have been included, although they have not yet been implemented; these include functions for recognizing isomorphisms and for using transpositions. We have left these for future iterations of our game.

**Sample Initial Menu:**

The user can select from three game-play options: Player vs. AI, Player vs. Player, and AI vs. AI

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg1.png" alt="RMimg1" style="zoom:50%;" />



For games played against the AI, the player may additionally select the game's difficulty (the depth to which the game will search the game tree for the AI's next-move) and whether they play first or second:

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg2.png" alt="RMimg2" style="zoom:50%;" />



**In-Game Interface:**

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg3.png" alt="RMimg3" style="zoom:67%;" />

The in-game interface allows for the user to access a help-menu with the above options. The player enters their move as two tuples, a coordinate for each of the dots they want to connect with a line.

## Sources

The following were referenced at different points of our assignment's development:

https://www.cs.rit.edu/~csci142/Labs/02/doc/game/package-summary.html

https://www2.cs.duke.edu/courses/fall01/cps006/dr/a/asn6/

https://stackoverflow.com/questions/4764787/data-structure-for-game-dots-and-boxes

https://wilson.engr.wisc.edu/boxes/method/

 The algorithm for the minimax and alpha-beta is adapted from the following website:

https://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html
