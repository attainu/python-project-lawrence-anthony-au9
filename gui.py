# File containing code crucial for GUI aspect of the chess program

import pygame
import os

# Loading all GUI resources
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
