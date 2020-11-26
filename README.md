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

#### **Sample Initial Menu:**

The user can select from three game-play options: Player vs. AI, Player vs. Player, and AI vs. AI

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg1.png" alt="RMimg1" style="zoom:50%;" />





For games played against the AI, the player may additionally select the game's difficulty (the depth to which the game will search the game tree for the AI's next-move) and whether they play first or second:

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg2.png" alt="RMimg2" style="zoom:50%;" />



#### **In-Game Interface:**

<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/RMimg3.png" alt="RMimg3" style="zoom:50%;"/>

The in-game interface allows for the user to access a help-menu with the above options. The player enters their move as two tuples, a coordinate for each of the dots they want to connect with a line.

## Data

| Depth | Depth     |              1 |                  2 |                     3 |                       4 |                          5 |
| :---: | --------- | -------------: | -----------------: | --------------------: | ----------------------: | -------------------------: |
|  2x2  | Seconds   |       0.100357 |           0.209773 |              0.935980 |                2.175184 |                   8.914355 |
|       | No. Nodes |    11x10 = 110 |      11x10x9 = 990 |     11x10x9x8 = 7,920 |    11x10x9x8x7 = 55,440 |    11x10x9x8x7x6 = 332,640 |
|       |           |                |                    |                       |                         |                            |
|  3x3  | Seconds   |       0.836551 |           0.785330 |             18.826792 |               52.928475 |                 495.647413 |
|       | No. Nodes |    23x22 = 506 |  23x22x21 = 10,626 | 23x22x21x20 = 212,520 | 23x22x21x20x19 =  4.0e6 |  23x22x21x20x19x18 = 7.2e7 |
|       |           |                |                    |                       |                         |                            |
|  4x4  | Seconds   |       4.484663 |          12.049024 |            169.886210 |              514.022982 |                     ------ |
|       | No. Nodes | 39x38 =  1,482 |  39x38x37 = 54,834 |   39x38x37x36 = 1.9e6 |  39x38x37x36x35 = 6.9e7 |  39x38x37x36x35x34 = 2.3e9 |
|       |           |                |                    |                       |                         |                            |
|  5x5  | Seconds   |      15.397095 |          45.495085 |            953.262535 |                  ------ |                     ------ |
|       | No. Nodes |  59x58 = 3,422 | 59x58x57 = 195,054 |   59x58x57x56 = 1.1e7 |  59x58x57x56x55 = 6.0e8 | 59x58x57x56x55x54 = 3.2e10 |

<p align="center">
  <img width="380" height="220" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph1.jpg">
  <img width="380" height="220" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph2.jpg">
  <img width="380" height="220" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph3.jpg">
</p>

## Sources

The following were referenced at different points of our assignment's development:

https://www.cs.rit.edu/~csci142/Labs/02/doc/game/package-summary.html

https://www2.cs.duke.edu/courses/fall01/cps006/dr/a/asn6/

https://stackoverflow.com/questions/4764787/data-structure-for-game-dots-and-boxes

https://wilson.engr.wisc.edu/boxes/method/

 The algorithm for the minimax and alpha-beta is adapted from the following website:

https://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html
