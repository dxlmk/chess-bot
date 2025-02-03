import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def get_piece_at(self, loc):
        return self.board.piece_at(loc)
    
    def get_svg(self, size):
        return chess.svg.board(board=self.board, size=480)
    
    def make_move(self, pos, new_pos):
        move = chess.Move(pos, new_pos)
        if move in self.board.legal_moves:
            self.board.push(move)