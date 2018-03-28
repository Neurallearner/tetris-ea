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

# run the genetic algorithm
for generation in range(0, max_generations):
    print 'Generation ' + str(generation)

    # run test for each player in a single generation
    fitness = {}
    for player in players:
        fitness[player] = 0
        for trial in range(0, num_trials):
            player.new_game()
            num_moves = 0
            while player.tetris.ongoing_game and num_moves < max_moves:
                num_moves += 1
                player.make_move()
            fitness[player] += -player.tetris.score / (max_moves * num_trials)
            print 'Trial '+str(trial+1)+':', player.tetris.score, player.params
            sorted_players = sorted(fitness.items(), key=operator.itemgetter(1))

    print fitness.values()
