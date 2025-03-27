import re
class Game():
    def __init__(self):
        self.turn: str = 'X'
        self.tie: bool = False
        self.winner: str | None = None
        self.board: dict[str, str] = {
            'a1': ' ',
            'a2': ' ',
            'a3': ' ',
            'b1': ' ',
            'b2': ' ',
            'b3': ' ',
            'c1': ' ',
            'c2': ' ',
            'c3': ' '
        }
    
    def switch_player(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def check_a_win(self, p1, p2, p3):
        b = self.board
        return b[p1] if b[p1] == b[p2] == b[p3] != ' ' else False

    def check_for_winner(self):
        w1 = self.check_a_win('a1', 'a2', 'a3')
        w2 = self.check_a_win('b1', 'b2', 'b3')
        w3 = self.check_a_win('c1', 'c2', 'c3')
        w4 = self.check_a_win('a1', 'b1', 'c1')
        w5 = self.check_a_win('a2', 'b2', 'c2')
        w6 = self.check_a_win('a3', 'b3', 'c3')
        w7 = self.check_a_win('a1', 'b2', 'c3')
        w8 = self.check_a_win('a3', 'b2', 'c1')
        return w1 or w2 or w3 or w4 or w5 or w6 or w7 or w8

    def prompt(self):
        move = input(f"Player {self.turn}, choose a legal move (ex.: A1): ")
        valid_move = re.match(r'^[a|b|c][1|2|3]$', move.lower())
        # check move validity, re-prompt if invalid
        while not valid_move or self.board[move.lower()] != ' ':
            print(f"Move {move} is not legal.")
            move = input(f"Player {self.turn}, choose a LEGAL move: ")
            valid_move = re.match(r'^[a|b|c][1|2|3]$', move.lower())
        # play the valid move
        self.board[move.lower()] = self.turn
        # check for a winner
        if self.check_for_winner():
            self.winner = self.turn
        else:
            self.switch_player()

    def show_message(self):
        if self.tie:
            print('wow another tie. how inspriring')
        # add logic for checking X/O wins
        else:
            print(f"It's {self.turn}'s turn:")

    def show_board(self):
        b = self.board
        print(f"""
   A   B   C
              
1  {b['a1']} | {b['b1']} | {b['c1']}
   ---------
2  {b['a2']} | {b['b2']} | {b['c2']}
   ---------
3  {b['a3']} | {b['b3']} | {b['c3']}
        """)
        # call method to prompt for a move
    
    def play_game(self):
        print('Pelcome po Py-Pac-Poe!\n')
        while not self.winner:
            self.show_message()
            self.show_board()
            self.prompt()
        self.show_board()
        print(f"Congratulations! {self.winner} wins.")


# instantiate and play
g = Game()
g.play_game()
# print(g.check_for_winner('a1', 'a2', 'a3'))
