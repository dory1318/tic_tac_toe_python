from board import *
from game import *
import pygame

class TicTac():

    def run_game(self):
        pygame.init()
        BLACK = (  0,   0,   0)
        WHITE = (255, 255, 255)
        size = [400, 300]
        screen = pygame.display.set_mode(size)

        player1 = "x"
        player2 = "o"
        game_over = False
        exit_flag = False
        while game_over == False and exit_flag == False: # looping until the end of the game
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # so we can quit the game anytime
                    exit_flag = True

def main():
    my_game = TicTac()
    my_game.run_game()

if __name__ == "__main__":
    main()
