'''
Abstract data types for the a game of Tetris and a Tetris board.
'''

import random
import pygame
import time

# the amount of time for the screen to pause between each step downward for the tetromino
pause_interval = 0.01

colors = [
    (0, 0, 0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218),
    (35, 35, 35)  # Helper color for background grid
]

white = (255, 255, 255)

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

max_rotations = [3, 1, 1, 3, 3, 1, 0]


# rotate a tetromino in the clockwise direction
def rotate_clockwise(shape):
    return [[shape[y][x]
             for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


# the abstract data type for a Tetris board
class Board(object):
    width = 10
    height = 22

    # constructs a Board object
    def __init__(self, grid=[[0 for __ in range(1, width + 1)] for __ in range(1, height + 1)]):
        self.grid = [[0 for __ in range(1, self.width + 1)] for __ in range(1, self.height + 1)]
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                self.grid[x][y] = grid[x][y]
        self.rows_cleared = 0
        self.num_tetrises = 0

    # test to see if a particular tetromino at a particular position does not run off the grid
    def fits_width(self, shape, offset):
        return offset >= 0 and offset + len(shape[0]) <= self.width

    # drop a tetromino into the Tetris board
    def drop(self, shape, offset):

        # check if shape does not run off sides of board
        if not self.fits_width(shape, offset):
            return -1

        # store useful variables
        board = self.grid
        shape_width = len(shape[0])
        shape_height = len(shape)
        min_dist = 100
        row_id = 0
        min_up_drop = 0

        # Find the maximum number of boxes the shape can drop
        for x in range(0, shape_width):
            down_drop = 0
            while down_drop < self.height and board[down_drop][offset + x] == 0:
                down_drop += 1
            up_drop = 0
            while shape[len(shape) - 1 - up_drop][x] == 0:
                up_drop += 1
            total_drop = down_drop + up_drop
            if total_drop < min_dist:
                min_dist = total_drop
                row_id = down_drop
                min_up_drop = up_drop

        # Check to make sure shape does not run off top of board (returns -1 to indicate game over)
        if min_dist < shape_height:
            return -1

        # Update the board to reflect the dropped shape
        for x in range(0, len(shape)):
            for y in range(0, len(shape[0])):
                board[row_id - len(shape) + x + min_up_drop][offset + y] += shape[x][y]

        # Check for rows that are full and delete them
        num_deleted = 0
        for x in range(row_id - len(shape) + min_up_drop, row_id + min_up_drop):
            full_row = True
            for y in range(0, Board.width):
                if board[x][y] == 0:
                    full_row = False
            if full_row:
                self.delete_row(x)
                num_deleted += 1
        if num_deleted == 4:
            self.num_tetrises += 1
        return num_deleted

    # deletes a row in the Tetris board
    def delete_row(self, row):
        self.rows_cleared += 1
        for x in range(row, 0, -1):
            for y in range(0, self.width):
                self.grid[x][y] = self.grid[x-1][y]
        for y in range(0, self.width):
            self.grid[0][y] = 0


# abstract data type for a Tetris object
class Tetris(object):

    points = [0, 2, 5, 15, 60]

    # constructor
    def __init__(self):
        self.board = Board()
        self.score = 0
        random.seed(random.uniform(1, 1000))
        self.current_shape = random.randint(0, 6)
        self.next_shape = random.randint(0, 6)
        self.ongoing_game = True

    # drop a tetromino at the specified position in the board
    def make_move(self, num_rotations, offset):
        if self.ongoing_game:
            shape = tetris_shapes[self.current_shape]
            self.current_shape = self.next_shape
            self.next_shape = random.randint(0, 6)
            for i in range(0, num_rotations):
                shape = rotate_clockwise(shape)
            rows_cleared = self.board.drop(shape, offset)
            if rows_cleared == -1:
                # print 'Game Over'
                # print 'Score: ' + str(self.score)
                self.ongoing_game = False
            else:
                self.score += self.points[rows_cleared]
            return rows_cleared
        else:
            print 'The game is over, stop trying to make a move.'


# Uncomment the following code to play tetris using keyboard input and pygame animation.

# game = Tetris()
# pygame.init()
# screen = pygame.display.set_mode((300,450))
# screen.fill(white)
#
# while game.ongoing_game:
#     for row in game.board.grid:
#         print row
#     print 'Current Shape:'
#     for row in tetris_shapes[game.current_shape]:
#         print row
#     print 'Next Shape:'
#     for row in tetris_shapes[game.next_shape]:
#         print row
#     print 'Current Score: ' + str(game.score)
#     num_rotations = input('Number of rotations: ')
#     offset = input('Offset by: ')
#     # num_rotations = random.randint(0, 3)
#     # offset = random.randint(0, 7)
#     game.make_move(num_rotations, offset)
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
#     pygame.display.update()
#     time.sleep(pause_interval)
