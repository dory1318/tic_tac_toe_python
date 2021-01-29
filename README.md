
# Noughts & Crosses - Tic Tac Toe
# :o: :x: :o:
# :x: :o: :x:
# :o: :x: :o:

---------

### To collaborate:
``
git clone https://github.com/dory1318/tic_tac_toe_python
``
### to install dependencies:
``pip3 install pytest``

``pip3 install pygame``

### to run the test:
``python3 test_game.py``

``pytest``

### to run game:
``python3 tictac.py``

----------

### Background story:
For our final project at Makers we chose the game Connect4 for our Machine Learning project. Being a ML project we didn't write the game from scratch, we used an existing code and focused on getting experience with ML technologies. Since that project, I fell in love with Python and wanted to see if I could build something similar by myself. So I picked Tic Tac Toe game, which is a well-known tech test at job interviews, and experimented with this new (well, for me) language.

#### The rules of tic-tac-toe are as follows:

- There are two players in the game (X and O)
- Players take turns until the game is over
- A player can claim a field if it is not already taken
- A turn ends when a player claims a field
- A player wins if they claim all the fields in a row, column or diagonal
- A game is over if a player wins
- A game is over when all fields are taken
- checks for winner
- checks for full board (or drawn)

### Achievement/things I have learned so far/things I am happy about:
:revolving_hearts: <i> TDD the Game class with 100% coverage </i>

:revolving_hearts: <i> successfully used numpy for my board </i>

:revolving_hearts: <i> it can make a move based on the given coordinates </i>

:revolving_hearts: <i> game starts with player1 all the time </i>

:revolving_hearts: <i> switches turn between player1 and player -1 </i>

:revolving_hearts: <i> if player attempts to choose a field that is alrady taken, they have to re-try </i>

:revolving_hearts: <i> it can tell who is the winner (if there is any) </i>

:revolving_hearts: <i> it can tell if board is full = drawn </i>

:revolving_hearts: <i> done some nice refactoring </i>

:revolving_hearts: <i> successfully used pygame for the "shiny & pretty" part </i>

:revolving_hearts: <i> can load pictures </i>

:revolving_hearts: <i> can resize pictures </i>

:revolving_hearts: <i> can give coordinates for picture location </i>

:revolving_hearts: <i> can create, draw, handle rectangles </i>

:revolving_hearts: <i> can get mouseclick location (position) </i>

:revolving_hearts: <i> for mouseclick, it places the X or the O within the rectangle </i>

:revolving_hearts: <i> I have had lots of fun building it, enjoyed writing the game and learned a lot! </i>

### Things that are missing/need to be learned/need to be changed
:broken_heart: <i> so far, after winning/drawn, information is only visible from command line. It would be nice if window would display the info </i>

:broken_heart: <i> new issue introduced: need to handle the "game over" scenario </i>

:broken_heart: <i> a nicer look altogether </i>
