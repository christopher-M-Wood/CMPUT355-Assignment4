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
| Depth | Depth      |               1 |                   2 |                      3 |                        4 |                           5 |
|:-----:|------------|----------------:|--------------------:|-----------------------:|-------------------------:|----------------------------:|
| 2x2   | Seconds    |        0.104203 |            0.104114 |               0.241327 |                 0.245682 |                    1.023649 |
|       |  No. Nodes |     11*10 = 110 |       11*10*9 = 990 |      11*10*9*8 = 7,920 |     11*10*9*8*7 = 55,440 |     11*10*9*8*7*6 = 332,640 |
|       |            |                 |                     |                        |                          |                             |
| 3x3   | Seconds    |        0.836551 |            0.902180 |               2.416159 |                 2.433585 |                   21.347394 |
|       |  No. Nodes |     23*22 = 506 |  23*22*21 = 10,626  |  23*22*21*20 = 212,520 |  23*22*21*20*19 =  4.0e6 |   23*22*21*20*19*18 = 7.2e7 |
|       |            |                 |                     |                        |                          |                             |
| 4x4   | Seconds    |        4.458014 |            4.515426 |              12.817606 |                12.994235 |                  180.560134 |
|       |  No. Nodes |  39*38 =  1,482 |   39*38*37 = 54,834 |    39*38*37*36 = 1.9e6 |   39*38*37*36*35 = 6.9e7 |   39*38*37*36*35*34 = 2.3e9 |
|       |            |                 |                     |                        |                          |                             |
| 5x5   | Seconds    |       16.059714 |           16.187346 |              46.964550 |                47.005949 |                      ------ |
|       |  No. Nodes |   59*58 = 3,422 |  59*58*57 = 195,054 |   59*58*57*56 = 1.1e7  |   59*58*57*56*55 = 6.0e8 |  59*58*57*56*55*54 = 3.2e10 |

<p align="center">
  <img width="520" height="339" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph1.jpg">
  <img width="520" height="339" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph2.jpg">
  <img width="520" height="339" src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/Graph3.jpg">
</p>

## Demo
Full Demo available here: https://youtu.be/ieTv5IVZg8A
<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/PvP.gif" alt="Player versus Player Demo" title="Player versus Player Demo" width="500"/>
<img src="https://github.com/christopher-M-Wood/CMPUT355-Assignment4/blob/master/AIvAI.gif" alt="AI as player 1 versus AI as player 2" title="AI versus AI" width="500"/>
## Sources

The following were referenced at different points of our assignment's development:

https://www.cs.rit.edu/~csci142/Labs/02/doc/game/package-summary.html

https://www2.cs.duke.edu/courses/fall01/cps006/dr/a/asn6/

https://stackoverflow.com/questions/4764787/data-structure-for-game-dots-and-boxes

https://wilson.engr.wisc.edu/boxes/method/

 The algorithm for the minimax and alpha-beta is adapted from the following website:

https://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html
