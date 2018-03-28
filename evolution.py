'''
The following code runs a genetic algorithm on a population of candidate Tetris players with randomly initialized
defining parameters.
'''

from player import *
import random
import operator

# set the parameters for the genetic algorithm
num_trials = 5
num_players = 100
max_generations = 30
max_moves = 200.0
mutation_rate = 0.25
sigma = 0.1 # mutations are done on a Gaussian Distribution, sigma is the standard deviation of the distribution

# initialize the players with randomized parameters
players = [Player([random.uniform(-1, 1) for i in range(0, 10)]) for j in range(0, num_players)]