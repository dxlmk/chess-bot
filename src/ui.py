import tkinter as tk
from board import ChessBoard
import pygame
import os

# screen constants
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
SQUARE_SIZE = 60

# Colors
PURPLE = (149,122,176)
GRAY = (224,213,234)
WHITE  = (255,255,255)
BLACK = (0,0,0)
GREEN = (124,149,132)
LIME = (201,211,144)

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
    def __init__(self, screen):
        self.screen = screen
        self.board = ChessBoard()
        self.font = pygame.font.Font(None, 48)
        self.selected_square = None

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
            self.screen.fill((0, 0, 0))
            self.draw_board()

            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())
            
            pygame.display.flip()
        pygame.quit()
        
    def handle_click(self, mouse_pos):
        new_col = mouse_pos[0] // SQUARE_SIZE
        new_row = 7-(mouse_pos[1] // SQUARE_SIZE)

        if self.selected_square:
            old_row = self.selected_square[0]
            old_col = self.selected_square[1]

            # If a piece is already selected, attempt the move
            self.board.make_move(old_row, old_col, new_row, new_col)
            self.selected_square = None  # Deselect after move
        else:
            # Select the clicked square
            if self.board.get_piece_at(new_row*8 + new_col):
                self.selected_square = (new_row, new_col)


    

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                #Draw board
                pygame.draw.rect(self.screen, 
                                 GRAY if (row + col) % 2 == 0 else PURPLE, 
                                 (col * SQUARE_SIZE, (7-row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                #Draw highlights on previous move squares
                if self.board.prev_move[0] == (row*8+col):
                    pygame.draw.rect(self.screen, LIME, (col * SQUARE_SIZE, (7-row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if self.board.prev_move[1] == (row*8+col):
                    pygame.draw.rect(self.screen, LIME, (col * SQUARE_SIZE, (7-row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                #Draw highlighted square
                if self.selected_square == (row, col):
                    pygame.draw.rect(self.screen, GREEN, 
                                     (col * SQUARE_SIZE, (7-row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                #Draw pieces 
                piece = self.board.get_piece_at(row * 8 + col)
                if piece:
                    piece_symbol = piece.symbol()
                    if piece_symbol in self.symbols:
                        # Draw the piece on the square
                        self.screen.blit(self.symbols[piece_symbol], 
                                         (col * SQUARE_SIZE, (7-row) * SQUARE_SIZE))
                        
                if self.selected_square and (row, col) in self.board.get_legal_moves(*self.selected_square):
                    pygame.draw.circle(self.screen, GREEN, 
                    (col * SQUARE_SIZE + SQUARE_SIZE/2, (7-row) * SQUARE_SIZE + SQUARE_SIZE/2), SQUARE_SIZE/8)


    
def start_ui():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Chess')

    ui = UI(screen)
    ui.run()