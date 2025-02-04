import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()
        self.prev_move = (None, None)

    def get_piece_at(self, loc):
        return self.board.piece_at(loc)
    
    def make_move(self, old_row, old_col, new_row, new_col):
        old_square = chess.square(old_col, old_row)
        new_square = chess.square(new_col, new_row)

        move = chess.Move(old_square, new_square)

        if move in self.board.legal_moves:
            self.board.push(move)
            self.prev_move = (old_square, new_square)
    
    def get_legal_moves(self, row, col):
        square = chess.square(col, row)
        legal_moves = [
            (chess.square_rank(move.to_square), chess.square_file(move.to_square)) 
            for move in self.board.legal_moves if move.from_square == square
        ]
        return legal_moves