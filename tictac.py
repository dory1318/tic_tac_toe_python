from board import *
from game import *
import pygame
import math

class TicTac():

    BLACK = (  0,   0,   0)
    LIGHT_ROSE = (255, 179, 230)
    PINK = (255, 26, 179)
    LILA = (153, 102, 255)
    size = [510, 450]
    SCREEN = pygame.display.set_mode(size)

    player1 = "x"
    player2 = "o"
    current_move = "x"

    NUM_COLS = 3
    NUM_ROWS = 3
    SQUARESIZE = 50
    WIDTH = NUM_COLS * SQUARESIZE
    HEIGHT = NUM_ROWS * SQUARESIZE
    SIZE = (WIDTH, HEIGHT)
    RADIUS = int(SQUARESIZE / 2 - 5)

    def draw_board(self, board):

        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 100, 100), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 200, 100), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 300, 100), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 100, 200), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 200, 200), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 300, 200), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 100, 300), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 200, 300), 5)
        pygame.draw.rect(self.SCREEN, self.PINK, (100, 100, 300, 300), 5)

    def run_game(self):
        pygame.init()
        self.SCREEN.fill(self.LIGHT_ROSE)
        self.draw_board(Game(Board().empty_board).new_board)
        pygame.display.update()

        game_over = False
        exit_flag = False
        while game_over == False and exit_flag == False: # looping until the end of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # so we can quit the game anytime
                    exit_flag = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # (mouseX, mouseY) = pygame.mouse.get_pos()
                    # (column, row) = map_mouse_to_board(mouseX, mouseY)
                    # pygame.draw.circle(self.SCREEN, self.BLACK, (200, 50), 40, 5)
                    posx = event.pos[0]
                    posy = event.pos[1]
                    if self.player1:
                        pygame.draw.circle(self.SCREEN, self.LILA, (posx, posy), 40, 5)
                        # pygame.draw.rect(self.SCREEN, self.BLACK, (0,0, self.WIDTH, self.SQUARESIZE))
                        move = int(math.floor(posx/self.SQUARESIZE))
                    else:
                        pygame.draw.circle(self.SCREEN, self.YELLOW, (posx, posy), 40, 5)

                    pygame.display.update()

                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # pygame.draw.rect(self.SCREEN, self.BLACK, (0,0, self.WIDTH, self.SQUARESIZE))
                    # posx = event.pos[0]
                    # move = int(math.floor(posx/self.SQUARESIZE))
                         # pygame.draw.circle(screen, BLACK, (200, 50), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (100, 50), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 50), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (200, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (100, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (200, 250), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (100, 250), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 250), 40, 5)

                         # pygame.draw.circle(screen, BLACK, (100, 50), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 50), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (200, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (100, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 150), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (200, 250), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (100, 250), 40, 5)
                         # pygame.draw.circle(screen, BLACK, (300, 250), 40, 5)
                         # pygame.display.update()
                    # pygame.quit()

def main():
    my_game = TicTac()
    my_game.run_game()

if __name__ == "__main__":
    main()
