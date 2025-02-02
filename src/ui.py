import tkinter as tk
from board import ChessBoard
import pygame
import os

# Window constants
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
SQUARE_SIZE = 60

# Colors
PURPLE = (149,122,176)
GRAY = (224,213,234)
WHITE  = (255,255,255)
BLACK = (0,0,0)

# Filepath for images
PIECES_IMAGES = {
    'K': 'images/wK.png', 'Q': 'images/wQ.png',
    'R': 'images/wR.png', 'N': 'images/wN.png',
    'B': 'images/wB.png', 'P': 'images/wP.png',
    'k': 'images/bK.png', 'q': 'images/bQ.png',
    'r': 'images/bR.png', 'n': 'images/bN.png',
    'b': 'images/bB.png', 'p': 'images/bP.png'
}

class UI:
    def __init__(self, window):
        self.window = window
        self.board = ChessBoard()
        self.font = pygame.font.Font(None, 48)

        # Load the images for the chess pieces
        self.symbols = {}
        for piece, path in PIECES_IMAGES.items():
            if os.path.exists(path):
                self.symbols[piece] = pygame.image.load(path)
                self.symbols[piece] = pygame.transform.scale(self.symbols[piece], (SQUARE_SIZE, SQUARE_SIZE))

    def run(self):
        # Run until the user quits the game
        running = True
        while running:
            self.window.fill((0, 0, 0))
            self.draw_chess_board()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()
        pygame.quit()
        
    
    def draw_chess_board(self):
        for row in range(8):
            for col in range(8):
                #Draw board
                pygame.draw.rect(self.window, 
                                 GRAY if (row + col) % 2 == 0 else PURPLE, 
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                #Draw pieces
                piece = self.board.get_piece_at((7 - row) * 8 + col)
                
                if piece:
                    piece_symbol = piece.symbol()
                    if piece_symbol in self.symbols:
                        # Draw the piece on the square
                        self.window.blit(self.symbols[piece_symbol], 
                                         (col * SQUARE_SIZE, row * SQUARE_SIZE))


    
def start_ui():
    pygame.init()
    window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Chess')

    ui = UI(window)
    ui.run()