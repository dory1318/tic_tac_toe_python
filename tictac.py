from game import *
import pygame
import math

class TicTac(Game):

    cross = pygame.image.load(r'x-button.png')
    circle = pygame.image.load(r'hula-hoop-2.png')
    CROSS = pygame.transform.smoothscale(cross, (60,60))
    CIRCLE = pygame.transform.smoothscale(circle, (70,70))
    BLACK = (  0,   0,   0)
    LIGHT_ROSE = (255, 179, 230)
    PINK = (255, 26, 179)
    LILA = (153, 102, 255)
    size = [510, 450]
    SCREEN = pygame.display.set_mode(size)
    COLS_AND_ROWS = {
        "col_1_row_1": pygame.Rect(100, 100, 100, 100), # [0][0]
        "col_2_row_1": pygame.Rect(200, 100, 100, 100), # [0][1]
        "col_3_row_1": pygame.Rect(300, 100, 100, 100), # [0][2]
        "col_1_row_2": pygame.Rect(100, 200, 100, 100), # [1][0]
        "col_2_row_2": pygame.Rect(200, 200, 100, 100), # [1][1]
        "col_3_row_2": pygame.Rect(300, 200, 100, 100), # [1][2]
        "col_1_row_3": pygame.Rect(100, 300, 100, 100), # [2][0]
        "col_2_row_3": pygame.Rect(200, 300, 100, 100), # [2][1]
        "col_3_row_3": pygame.Rect(300, 300, 100, 100)  # [2][2]
    }

    def draw_board(self, board):
        for i in self.COLS_AND_ROWS:
            pygame.draw.rect(self.SCREEN, self.PINK, (self.COLS_AND_ROWS[i]), 5)

    def mouse_click_on_board(self, x, y):
        if (self.COLS_AND_ROWS['col_1_row_1'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_1_row_2'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_1_row_3'].collidepoint(x, y)):
            column = 0
        elif (self.COLS_AND_ROWS['col_2_row_1'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_2_row_2'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_2_row_3'].collidepoint(x, y)):
            column = 1
        elif (self.COLS_AND_ROWS['col_3_row_1'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_3_row_2'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_3_row_3'].collidepoint(x, y)):
            column = 2

        if (self.COLS_AND_ROWS['col_1_row_1'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_2_row_1'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_3_row_1'].collidepoint(x, y)):
            row = 0
        elif (self.COLS_AND_ROWS['col_1_row_2'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_2_row_2'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_3_row_2'].collidepoint(x, y)):
            row = 1
        elif (self.COLS_AND_ROWS['col_1_row_3'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_2_row_3'].collidepoint(x, y)) or (self.COLS_AND_ROWS['col_3_row_3'].collidepoint(x, y)):
            row = 2

        return column, row

    def draw_on_board(self, shape, x, y):
        if self.COLS_AND_ROWS['col_1_row_1'].collidepoint(x, y):
            self.SCREEN.blit(shape, (115, 115))
        elif self.COLS_AND_ROWS['col_1_row_2'].collidepoint(x, y):
            self.SCREEN.blit(shape, (215, 115))
        elif self.COLS_AND_ROWS['col_1_row_3'].collidepoint(x, y):
            self.SCREEN.blit(shape, (315, 115))
        elif self.COLS_AND_ROWS['col_2_row_1'].collidepoint(x, y):
            self.SCREEN.blit(shape, (115, 215))
        elif self.COLS_AND_ROWS['col_2_row_2'].collidepoint(x, y):
            self.SCREEN.blit(shape, (215, 215))
        elif self.COLS_AND_ROWS['col_2_row_3'].collidepoint(x, y):
            self.SCREEN.blit(shape, (315, 215))
        elif self.COLS_AND_ROWS['col_3_row_1'].collidepoint(x, y):
            self.SCREEN.blit(shape, (115, 315))
        elif self.COLS_AND_ROWS['col_3_row_2'].collidepoint(x, y):
            self.SCREEN.blit(shape, (215, 315))
        elif self.COLS_AND_ROWS['col_3_row_3'].collidepoint(x, y):
            self.SCREEN.blit(shape, (315, 315))


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
                    (column, row) = self.mouse_click_on_board(mouseY, mouseX)
                    self.make_move(column, row)
                    if self.new_board[column, row] == 1:
                        self.draw_on_board(self.CROSS, mouseY, mouseX)
                    else:
                        self.draw_on_board(self.CIRCLE, mouseY, mouseX)

                    print(self.new_board)
                    if self.winner() is not None:
                        if self.winner() == 1:
                            print("X has won")
                            game_over = True
                        elif self.winner() == -1:
                            print(self.winner())
                            print("O has won")
                            game_over = True
                    else:
                        if self.full_board() == True:
                            print("It's a draw")
                            game_over = True

                    pygame.display.update()


def main():
    my_game = TicTac()
    my_game.run_game()

if __name__ == "__main__":
    main()
