import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
CELL_SIZE = WIDTH // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (66, 66, 66)
O_COLOR = (239, 231, 200)

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, X_COLOR,
                                 (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 80, row * CELL_SIZE + 80), 5)
                pygame.draw.line(screen, X_COLOR,
                                 (col * CELL_SIZE + 80, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 20, row * CELL_SIZE + 80), 5)
            
            elif board[row][col] == "O":
                pygame.draw.circle(screen, O_COLOR,
                                   (col * CELL_SIZE + 50, row * CELL_SIZE + 50),
                                   30, 5)
                
def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
               return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 -i] == player for i in range(3)):
        return True
    
    return False

