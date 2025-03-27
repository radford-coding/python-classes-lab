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

    def check_for_winner(self, p1, p2, p3):
        b = self.board
        return b[p1] if b[p1] == b[p2] == b[p3] != ' ' else False

    def prompt(self):
        move = input(f"Player {self.turn}, choose a legal move (ex.: A1): ")
        valid_move = re.match(r'^[a|b|c][1|2|3]$', move.lower())
        while not valid_move or self.board[move.lower()] != ' ':
            print(f"Move {move} is not legal.")
            move = input(f"Player {self.turn}, choose a LEGAL move: ")
            valid_move = re.match(r'^[a|b|c][1|2|3]$', move.lower())
        self.board[move.lower()] = self.turn
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


# instantiate and play
g = Game()
g.play_game()
# print(g.check_for_winner('a1', 'a2', 'a3'))
