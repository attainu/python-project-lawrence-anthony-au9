# File to store functions dealing with GUI aspect of chess program

import pygame
import os

# Load all resources
PSPRITE = pygame.image.load(os.path.join("images", "pieces.png"))
PIECES = ({}, {})
for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
    for side_flag in range(2):
        PIECES[side_flag][ptype] = PSPRITE.subsurface(
            (i*50, side_flag*50, 50, 50))

CHOOSE = pygame.image.load(os.path.join("images", "choose.jpg"))
CHECK = pygame.image.load(os.path.join("images", "check.jpg"))
STALEMATE = pygame.image.load(os.path.join("images", "stalemate.jpg"))
CHECKMATE = pygame.image.load(os.path.join("images", "checkmate.jpg"))


# Get user choice for pawn promotion

def getChoice(win, side_flag):
    win.blit(CHOOSE, (100, 0))
    win.blit(PIECES[side_flag]['q'], (200, 0))
    win.blit(PIECES[side_flag]['b'], (250, 0))
    win.blit(PIECES[side_flag]['r'], (300, 0))
    win.blit(PIECES[side_flag]['n'], (350, 0))
    pygame.display.update((0, 0, 500, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < event.pos[1] < 50:
                    if 200 < event.pos[0] < 250:
                        return "q"
                    elif 250 < event.pos[0] < 300:
                        return "b"
                    elif 300 < event.pos[0] < 350:
                        return "r"
                    elif 350 < event.pos[0] < 400:
                        return "n"


# Function to draw the chess board

def drawBoard(win):
    win.fill((100, 200, 200))
    for y in range(1, 9):
        for x in range(1, 9):
            if (x + y) % 2 == 0:
                pygame.draw.rect(win, (220, 240, 240),
                                 (50 * x, 50 * y, 50, 50))
            else:
                pygame.draw.rect(win, (180, 100, 30), (50 * x, 50 * y, 50, 50))


# Function to draw pieces on the screen

def drawPieces(win, board):
    for side_flag in range(2):
        for x, y, ptype in board[side_flag]:
            win.blit(PIECES[side_flag][ptype], (x * 50, y * 50))
