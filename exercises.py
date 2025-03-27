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