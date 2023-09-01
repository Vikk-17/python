ALL_SPACES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')   
# list('123456789') # The keys for a TTT board
X, O, BLANK = 'X', 'O', ' '     # constants for string values

# def main():
#     """Runs a game of tic tac toe."""
#     print("Welcome to tic-tac-toe!")
#     gameBoard = TTTBoard() # Create a TTT board object
#     currentPlayer, nextPlayer = X, O    # X goes first, O goes next.

#     while True:
#         print(gameBoard. getBoardStr())     # Display the board on the screen
#         # keep asking the player until they enter a number 1-9:
#         move = None
    # pass

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic tac toe board."""
        self._spaces = {}     # The board is represents as python dict
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All spaces start as blank.
    
    def drawBoard(self):
        """Return a text-representation of the board."""
        print(f'''
        {self._spaces['7']}
        ''')