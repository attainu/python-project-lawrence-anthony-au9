# Chess game project made by Lawrence Anthony

import os
import pygame
from gui import *
from chess import *


# Class containing objects required for Sounds. Currently it has only background music, plan
# to add more sounds in future

class Sound:
    def __init__(self):
        pygame.mixer.music.load(os.path.join("sounds", "background.ogg"))
        pygame.mixer.music.play(-1)


# Class that contains objects to handle GUI part of the program

class gui_logic:
    def __init__(self):
        pass

    # Function to get user choice for pawn promotion

    def getChoice(self, win, side_flag):
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

    def drawBoard(self, win):
        win.fill((100, 200, 200))
        for y in range(1, 9):
            for x in range(1, 9):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(win, (220, 240, 240),
                                     (50 * x, 50 * y, 50, 50))
                else:
                    pygame.draw.rect(win, (180, 100, 30),
                                     (50 * x, 50 * y, 50, 50))

    # Function to draw pieces on the screen

    def drawPieces(self, win, board):
        for side_flag in range(2):
            for x, y, ptype in board[side_flag]:
                win.blit(PIECES[side_flag][ptype], (x * 50, y * 50))


# Main driver Function for chess program
if __name__ == "__main__":

    # Initializing regular pygame stuff.
    pygame.init()
    clock = pygame.time.Clock()

    # Flag to toggle sound, to disable set music_flag to False, to enable set it to True
    music_flag = True
    if music_flag:
        m = Sound()

    # Initializing Pygame window where the game will be played and Window Title
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Simple 2 player Chess using Python')

    # Calling gui_logic class
    g = gui_logic()

    # Initialize chess variables

    # Flag that determines which side's turn it is. If it is 0, it is white's turn and if it is
    # 1, it is black's turn
    side_flag = 0

    board = (
        [[1, 7, "p"], [2, 7, "p"], [3, 7, "p"], [4, 7, "p"],
         [5, 7, "p"], [6, 7, "p"], [7, 7, "p"], [8, 7, "p"],
         [1, 8, "r"], [2, 8, "n"], [3, 8, "b"], [4, 8, "q"],
         [5, 8, "k"], [6, 8, "b"], [7, 8, "n"], [8, 8, "r"]
         ], [
            [1, 2, "p"], [2, 2, "p"], [3, 2, "p"], [4, 2, "p"],
            [5, 2, "p"], [6, 2, "p"], [7, 2, "p"], [8, 2, "p"],
            [1, 1, "r"], [2, 1, "n"], [3, 1, "b"], [4, 1, "q"],
            [5, 1, "k"], [6, 1, "b"], [7, 1, "n"], [8, 1, "r"]
        ])

    flags = [[True for _ in range(4)], None]

    # Lists that store x,y co-ordinate of current and previous mouse selection on pygame window
    sel = prevsel = [0, 0]

    # Main function for showing the chess board. We call it once every game loop.

    def showScreen(win, side_flag, board, flags, pos):
        g.drawBoard(win)
        if isEnd(side_flag, board, flags):
            if isChecked(side_flag, board):
                win.blit(CHECKMATE, (120, 0))
                win.blit(PIECES[side_flag]['k'], (270, 0))
            else:
                win.blit(STALEMATE, (150, 0))
        else:
            if isChecked(side_flag, board):
                win.blit(CHECK, (180, 0))

            if isOccupied(side_flag, board, pos):
                x, y = pos[0] * 50, pos[1] * 50
                pygame.draw.rect(win, (255, 255, 0), (x, y, 50, 50))
        g.drawPieces(win, board)

    # return getChoice only if pawn has reached promotion state

    def getPromote(win, side_flag, board, fro, to):
        if getType(side_flag, board, fro) == "p":
            if (side_flag == 0 and to[1] == 1) or (side_flag == 1 and to[1] == 8):
                return g.getChoice(win, side_flag)

    # Running game loop infinitely until the running flag becomes False
    running = True
    while running:

        clock.tick(30)

        # Iterating over events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    prevsel = sel
                    sel = [x, y]

                # If move is legal, we will do the move and update chess variables
                if isValidMove(side_flag, board, flags, prevsel, sel):
                    promote = getPromote(win, side_flag, board, prevsel, sel)
                    side_flag, board, flags = makeMove(
                        side_flag, board, prevsel, sel, flags, promote)
        # Show screen
        showScreen(win, side_flag, board, flags, sel)
        pygame.display.update()

    # Quit pygame
    pygame.quit()
