# TicTacToe
## **1. Summary**
The project involves implementing a Tic Tac Toe game using the minimax algorithm
and a graphical user interface (GUI) built with the Tkinter library in Python.
The Tic Tac Toe game will be implemented as a class that manages the game state and
provides functions for making moves, checking for a win or draw, and switching
between players. The minimax algorithm will be implemented as a function that takes
the current game state as input and returns the best move for the current player, based
on the assumption that the opponent will play optimally.
The GUI will consist of a 3x3 grid of cells, where each cell is either empty or contains
an X or an O symbol. The players will take turns clicking on an empty cell to place their
symbol.
To run the game, the user will need to start the GUI class, which will create an instance
of the Tic Tac Toe game and start the main loop. The main loop will display the current
state of the board, handle user input, and call the minimax function to determine the
computer's move (if applicable). The loop will continue until the game is over, at which
point it will display a message indicating the outcome (win, lose, or draw).
## **2. Previous Work In The Literature**
One common approach to implementing tic-tac-toe is to use the minimax algorithm,
which is a popular choice for decision-making in two-player games. The minimax
algorithm works by considering all of the possible moves that can be made by both
players, and then choosing the move that is most likely to lead to a win for the current
player (assuming that their opponent is also playing optimally).
Other approaches to implementing tic-tac-toe include using artificial neural networks,
genetic algorithms, and Monte Carlo tree search. These approaches have been shown to
be effective at playing tic-tac-toe at a high level, but they may be more complex to
implement and may require more computational resources.
In terms of user interfaces, tic-tac-toe has been implemented using a variety of methods,
including text-based interfaces, graphical interfaces, and web-based interfaces. The
choice of user interface will depend on the intended audience and the platform on which
the game will be played.
Overall, the literature on tic-tac-toe includes a wide range of approaches to
implementing the game logic and user interface, and there are many resources available
for those interested in learning more about the topic.
## **3. Description Of The Project**
###### **3.1 Implementation**
To implement a Tic Tac Toe game with the minimax algorithm in Python, I
followed these steps.
Defining the game state, In this case, the game state will be represented by the
current state of the tic-tac-toe board. I defined an array to store the board state and
a set of functions to manipulate it.
Defining the game rules, I define a set of rules that determine when the game is
over (e.g., when one player has won or when the board is full) and who the winner
is (if the game has ended). <br>
![image](https://user-images.githubusercontent.com/94220642/224927318-e3335147-7db5-4c55-ab97-96f1e1f8838a.png)
<br>
3. Description Of The Project
3.1 Implementation
To implement a Tic Tac Toe game with the minimax algorithm in Python, I
followed these steps.
Defining the game state, In this case, the game state will be represented by the
current state of the tic-tac-toe board. I defined an array to store the board state and
a set of functions to manipulate it.
Defining the game rules, I define a set of rules that determine when the game is
over (e.g., when one player has won or when the board is full) and who the winner
is (if the game has ended).
<br> **Implementation the minimax algorithm**, <br> The minimax algorithm involves
recursively considering all of the possible moves that can be made by both players,
and then choosing the move that is most likely to lead to a win for the current
player (assuming that their opponent is also playing optimally). I defined a
function that takes the current game state as input and returns the best move for the
current player. <br>
![image](https://user-images.githubusercontent.com/94220642/224927618-9bc426d3-8f38-4d7f-a926-e99486c4173b.png)
<br>
![image](https://user-images.githubusercontent.com/94220642/224927708-df1d2435-cfee-4bde-8204-b17b79460847.png)
![image](https://user-images.githubusercontent.com/94220642/224927734-0a01a8b5-dce3-41d5-a7ab-afcabb54de16.png)
![image](https://user-images.githubusercontent.com/94220642/224927772-b0012338-086e-447a-9f80-6f1e8ca02c37.png)
![image](https://user-images.githubusercontent.com/94220642/224927800-61247c95-50e0-49ff-9443-9d0871ef6a26.png)
<br>
![image](https://user-images.githubusercontent.com/94220642/224927826-e9515f21-4b6d-4b52-bc88-a4df6b8e75a7.png)


