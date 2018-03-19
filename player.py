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
        best_rots = 0
        best_offset = 0
        best_score = -float('inf')

        # iterate through all possible combinations of moves using the next two tetrominos
        current_grid = tetris_shapes[self.tetris.current_shape]
        next_grid = tetris_shapes[self.tetris.next_shape]
        for rot1 in range(0, max_rotations[self.tetris.current_shape] + 1):
            for offset1 in range(0, self.tetris.board.width - len(current_grid[0]) + 1):
                for rot2 in range(0, max_rotations[self.tetris.next_shape] + 1):
                    for offset2 in range(0, self.tetris.board.width - len(next_grid[0]) + 1):
                        candidate = Board(self.tetris.board.grid)
                        candidate.drop(current_grid, offset1)
                        candidate.drop(next_grid, offset2)
                        candidate_score = self.score(candidate)
                        if candidate_score > best_score:
                            best_score = candidate_score
                            best_rots = rot1
                            best_offset = offset1
                    next_grid = rotate_clockwise(next_grid)
            current_grid = rotate_clockwise(current_grid)
        self.tetris.make_move(best_rots, best_offset)
        return [best_rots, best_offset]

    # return the score of the Tetris board according to the initially assigned parameters
    def score(self, board):
        score = 0
        feats = self.features(board)
        for i in range(0, len(self.params)):
            score += self.params[i] * feats[i]
        return score

    # return the features array of a particular Tetris board
    def features(self, board_object):
        my_grid = board_object.grid
        heights = []
        for x in range(0, len(my_grid[0])):
            found_height = False
            for y in range(0, len(my_grid)):
                if not found_height and not my_grid[y][x] == 0:
                    heights.append(board_object.height - y)
                    found_height = True
                if not found_height and y == len(my_grid) - 1:
                    heights.append(0)

        # height of tallest column
        f1 = -1
        # sum of absolute value of difference between adjacent heights
        f2 = 0
        # number of pits
        f3 = 0
        min_height = float('inf')
        second_min_height = float('inf')
        for i in range(0, len(heights)):
            is_pit = True
            if i > 0 and heights[i] >= heights[i-1]:
                is_pit = False
            if i < len(heights)-1 and heights[i] >= heights[i+1]:
                is_pit = False
            if is_pit:
                f3 += 1
            if heights[i] < min_height:
                second_min_height = min_height
                min_height = heights[i]
            elif heights[i] < second_min_height:
                second_min_height = heights[i]
            if i > 0:
                f2 += abs(heights[i] - heights[i-1])
            if heights[i] > f1:
                f1 = heights[i]
        # number of tetrises that have been made in the board
        f4 = board_object.num_tetrises
        # difference between smallest height and second smallest height
        f5 = second_min_height - min_height
        # minimum height plus one
        f6 = min_height
        # sum of weights of blocks, where weight is the height of the block
        f7 = 0
        # number of vertically connected holes
        f8 = 0
        # total number of blocks
        f9 = 0
        # number of columns that contains at least one hole
        f10 = 0
        for y in range(0, len(my_grid[0])):
            found_hole = False
            for x in range(0, len(my_grid)):
                if not my_grid[x][y] == 0:
                    f7 += len(my_grid) - x
                    f9 += 1
                elif len(my_grid) - x < heights[y] and not my_grid[x - 1][y] == 0:
                    f8 += 1
                    if not found_hole:
                        f10 += 1
                        found_hole = True

        return [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]


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
