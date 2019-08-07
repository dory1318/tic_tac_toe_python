from game import *
import pygame
import math

class TicTac(Game):

    BLACK = (  0,   0,   0)
    LIGHT_ROSE = (255, 179, 230)
    PINK = (255, 26, 179)
    LILA = (153, 102, 255)
    size = [510, 450]
    SCREEN = pygame.display.set_mode(size)
    col_1_row_1 = pygame.Rect(100, 100, 100, 100) # [0][0]
    col_2_row_1 = pygame.Rect(200, 100, 100, 100) # [0][1]
    col_3_row_1 = pygame.Rect(300, 100, 100, 100) # [0][2]
    col_1_row_2 = pygame.Rect(100, 200, 100, 100) # [1][0]
    col_2_row_2 = pygame.Rect(200, 200, 100, 100) # [1][1]
    col_3_row_2 = pygame.Rect(300, 200, 100, 100) # [1][2]
    col_1_row_3 = pygame.Rect(100, 300, 100, 100) # [2][0]
    col_2_row_3 = pygame.Rect(200, 300, 100, 100) # [2][1]
    col_3_row_3 = pygame.Rect(300, 300, 100, 100) # [2][2]

    def draw_board(self, board):

        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_1_row_1), 5) # [0][0]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_2_row_1), 5) # [0][1]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_3_row_1), 5) # [0][2]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_1_row_2), 5) # [1][0]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_2_row_2), 5) # [1][1]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_3_row_2), 5) # [1][2]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_1_row_3), 5) # [2][0]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_2_row_3), 5) # [2][1]
        pygame.draw.rect(self.SCREEN, self.PINK, (self.col_3_row_3), 5) # [2][2]

    def mouse_click_on_board(self, x, y):
        if (self.col_1_row_1.collidepoint(x,y)) or (self.col_1_row_2.collidepoint(x,y)) or (self.col_1_row_3.collidepoint(x,y)):
            column = 0
        elif (self.col_2_row_1.collidepoint(x,y)) or (self.col_2_row_2.collidepoint(x,y)) or (self.col_2_row_3.collidepoint(x,y)):
            column = 1
        elif (self.col_3_row_1.collidepoint(x,y)) or (self.col_3_row_2.collidepoint(x,y)) or (self.col_3_row_3.collidepoint(x,y)):
            column = 2

        if (self.col_1_row_1.collidepoint(x,y)) or (self.col_2_row_1.collidepoint(x,y)) or (self.col_3_row_1.collidepoint(x,y)):
            row = 0
        elif (self.col_1_row_2.collidepoint(x,y)) or (self.col_2_row_2.collidepoint(x,y)) or (self.col_3_row_2.collidepoint(x,y)):
            row = 1
        elif (self.col_1_row_3.collidepoint(x,y)) or (self.col_2_row_3.collidepoint(x,y)) or (self.col_3_row_3.collidepoint(x,y)):
            row = 2

        return column, row



    def run_game(self):
        pygame.init()
        self.SCREEN.fill(self.LIGHT_ROSE)
        self.draw_board(self.new_board)
        pygame.display.update()

        game_over = False
        exit_flag = False
        while game_over == False and exit_flag == False: # looping until the end of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # so we can quit the game anytime
                    exit_flag = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    (column, row) = self.mouse_click_on_board(mouseX, mouseY)
                    print(column, row)

                    pygame.display.update()


def main():
    my_game = TicTac()
    my_game.run_game()

if __name__ == "__main__":
    main()
