'''
This is a Tic Tac Toe game.
'''
import random

class TicTacToe():
    '''
    Tic Tac Toe game main functions
    '''

    WIN_CONDITIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)             # Diagonal
    ]

    def __init__(self):
        '''
        Initial the game
        '''
        self.board = [" "] * 9
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def make_move(self, location):
        '''
        If the player is O, fill in the blank with O. If the player is X, fill in the blank with X.
        '''
        if self.board[location] == " ":
            self.board[location] = self.current_player
            if self.check_if_game_over():
                return
            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_current(self):
        '''
        Print current location.
        '''
        print("\n   --- Board ---")
        print("    1   2   3")
        for i in range(3):
            cell1 = self.board[i*3]
            cell2 = self.board[i*3+1]
            cell3 = self.board[i*3+2]
            row_display = f"{i+1}   {cell1} | {cell2} | {cell3}"
            print(row_display)
            if i < 2:
                print("   -----------")
        print()

    def print_result(self):
        '''
        Print result and winner.
        '''
        self.print_current()
        if self.winner:
            print(f"Winner is Player '{self.winner}'! ")
        else:
            print("Draw.")

    def check_if_game_over(self):
        '''
        Check whether the game is over.
        '''
        # Check for win
        for cond in self.WIN_CONDITIONS:
            if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] != " ":
                self.game_over = True
                self.winner = self.board[cond[0]]
                return True

        # Check for draw
        if " " not in self.board:
            self.game_over = True
            self.winner = None
            return True
        return False

    def human_turn(self):
        '''
        Human can operate on this turn.
        '''
        print(f"Player '{self.current_player}', it's your turn.")
        while True:
            try:
                row = int(input("Enter the row (1-3): "))
                col = int(input("Enter the column (1-3): "))

                if not (row in [1, 2, 3] and col in [1, 2, 3]):
                    print("Invalid input. Please enter numbers between 1 and 3.")
                    continue

                location = (row - 1) * 3 + (col - 1)
                if self.board[location] != " ":
                    print("Oops! That spot is already taken. Try again.")
                    continue

                self.make_move(location)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def pc_turn(self):
        '''
        PC will operate on this turn.
        '''
        available_moves = [i for i, spot in enumerate(self.board) if spot == " "]

        if available_moves:
            location = random.choice(available_moves)
            row = location // 3 + 1
            col = location % 3 + 1
            print(f"PC chooses row {row}, column {col}.")
            self.make_move(location)

def main():
    '''
    Start the game and show UI.
    '''
    game = TicTacToe()
    print("Let's play Tic-Tac-Toe!")
    print("You are 'X', and the PC is 'O'.")

    while not game.game_over:
        if game.current_player == 'X':
            game.print_current()
            game.human_turn()
        else:
            game.pc_turn()

        if game.game_over:
            break

    game.print_result()

if __name__ == "__main__":
    main()
