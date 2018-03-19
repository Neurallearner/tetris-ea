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

    players = []

    # add top players
    for i in range(0, int(0.2*num_players)):
        players.append(Player(sorted_players[i][0].params))
        print 'Added (survived): ', sorted_players[i][0].params

    # add mutated players
    for i in range(0, int(0.4 * num_players)):
        mutated_player = sorted_players[random.randint(0, num_players - 1)][0]
        mutated_params = [param for param in mutated_player.params]
        for j in range(0, len(mutated_params)):
            if random.random() < mutation_rate:
                mutated_params[j] += random.gauss(0, sigma)
        mutated_player = Player(mutated_params)
        players.append(mutated_player)
        print 'Added (mutate): ', mutated_player.params

    # add children of mated players
    while len(players) < num_players:
        parents = random.sample(0.4*range(num_players), 2)
        child_params = []
        for i in range(0, len(sorted_players[0][0].params)):
            if random.random() < 0.5:
                child_params.append(sorted_players[parents[0]][0].params[i])
            else:
                child_params.append(sorted_players[parents[1]][0].params[i])
        players.append(Player(child_params))
        print 'Added (child): ', child_params