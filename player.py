'''
The following is a Tetris Player class that is characterized by a set of numerical parameters plays the game of Tetris
using these parameters to make decisions about moves.
'''
from tetris import *
import pygame, time


# Tetris player class
class Player(object):

    # constructor takes in the defining set of parameters and starts a game of Tetris
    def __init__(self, params):
        self.params = params
        self.tetris = Tetris()

    # starts a new game of tetris
    def new_game(self):
        self.tetris = Tetris()

    # player makes a single move on the ongoing game of tetris
    def make_move(self):
        
        # TODO
        
        return

    # return the score of the Tetris board according to the initially assigned parameters
    def score(self, board):
        score = 0
        
        # TODO

        return score

    # return the features array of a particular Tetris board
    def features(self, board_object):
        my_grid = board_object.grid
        
        # TODO

        return


# Uncomment the following code to watch a player with specified input parameters play tetris.

# test = Player([-0.5925455859683959, -0.07882464790694166, 0.20735463222995953, 0.3124733405747875, -0.762437048043221, -1.0802513180718805, -0.7471643926937466, -0.784878429516275, 0.2851664863561476, -0.3306426596219414])
# game = test.tetris
# pygame.init()
# screen = pygame.display.set_mode((300,450))
# while game.ongoing_game:
#     screen.fill(white)
#     for row in game.board.grid:
#         print row
#     print 'Current Shape:'
#     for row in tetris_shapes[game.current_shape]:
#         print row
#     print 'Next Shape:'
#     for row in tetris_shapes[game.next_shape]:
#         print row
#     print 'Current Score: ' + str(game.score)
#
#     # raw_input('Press enter to make move:')
#
#     test.make_move()
#
#     for x in range(0, len(game.board.grid)):
#         for y in range(0, len(game.board.grid[0])):
#             entry = game.board.grid[x][y]
#             pygame.draw.rect(screen, colors[entry], (50+15*y, 50+15*x, 15, 15), 0)
#
#     next_shape = tetris_shapes[game.next_shape]
#     current_shape = tetris_shapes[game.current_shape]
#
#     for x in range(0, 4):
#         for y in range(0, 4):
#             if x < len(current_shape) and y < len(current_shape[0]) and not current_shape[x][y] == 0:
#                 entry = current_shape[x][y]
#                 pygame.draw.rect(screen, colors[entry], (200+15*y, 50+15*x, 15, 15), 0)
#             else:
#                 pygame.draw.rect(screen, white, (200+15*y, 50+15*x, 15, 15), 0)
#
#     for x in range(0, 4):
#         for y in range(0, 4):
#             if x < len(next_shape) and y < len(next_shape[0]) and not next_shape[x][y] == 0:
#                 entry = next_shape[x][y]
#                 pygame.draw.rect(screen, colors[entry], (200+15*y, 90+15*x, 15, 15), 0)
#             else:
#                 pygame.draw.rect(screen, white, (200+15*y, 90+15*x, 15, 15), 0)
#
#     # Display some text
#     font = pygame.font.Font(None, 36)
#     text = font.render('Score: ' + str(game.score), 1, (10, 10, 10))
#     textpos = text.get_rect()
#     textpos.centerx = screen.get_rect().centerx
#     screen.blit(text, textpos)
#
#     pygame.display.update()
#     time.sleep(pause_interval)