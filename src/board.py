import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()
        print(self.board)
        print(self.board.piece_at(0))

    def get_piece_at(self, loc):
        return self.board.piece_at(loc)
    
    def get_svg(self, size):
        return chess.svg.board(board=self.board, size=480)