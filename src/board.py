import chess

class Board:
    def __init__(self):
        self.board = chess.Board()
        print(self.board.piece_at(36))

    def piece_at(self, row, col):
        return self.board.piece_at(row+col)
        