import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()
        self.prev_move = (None, None)

    def get_piece_at(self, loc):
        return self.board.piece_at(loc)
    
    def get_svg(self, size):
        return chess.svg.board(board=self.board, size=480)
    
    def make_move(self, old_row, old_col, new_row, new_col):
        old_pos = old_row*8 + old_col
        new_pos = new_row*8 + new_col

        move = chess.Move(old_pos, new_pos)

        if move in self.board.legal_moves:
            self.board.push(move)
            self.prev_move = (old_pos, new_pos)