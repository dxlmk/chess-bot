import tkinter as tk
from board import Board
import pygame

# Window constants
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
SQUARE_SIZE = 60

# Colors
PURPLE = (149,122,176)
GRAY = (224,213,234)
WHITE  = (255,255,255)
BLACK = (0,0,0)

class UI:
    def __init__(self, window):
        self.window = window
        self.board = Board()
        self.font = pygame.font.Font(None, 48)

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
        for col in range(8):
            for row in range(8):
                #Draw board
                pygame.draw.rect(self.window, 
                                 GRAY if (row + col) % 2 == 0 else PURPLE, 
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                #Draw pieces

    
def start_ui():
    pygame.init()
    window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Chess')

    ui = UI(window)
    ui.run()