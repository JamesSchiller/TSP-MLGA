from random import randint
from random import random
from decimal import *

global chromosomes
global offsprings

chromosomes = []
offsprings = []

graph = {
  'connections': [
    ('a', 'b', 1), 
    ('a', 'c', 2), 
    ('b', 'd', 5), 
    ('c', 'd', 3), 
    ('d', 'e', 2), 
    ('d', 'f', 3), 
    ('e', 'f', 1), 
    ('e', 'g', 4), 
    ('f', 'g', 3), 
    ('d', 'i', 5), 
    ('i', 'j', 2), 
    ('j', 'h', 7), 
    ('h', 'c', 5), 
    ('f', 'i', 1)    
  ]
}

CHROMOSOMES = 6
GENES = len(graph['connections'])
GENERATIONS = 4
MUTATION_RATE = Decimal('1') / Decimal(GENES)
STRATEGIES = 4
MAX_WEIGHT = 10

for i in range(CHROMOSOMES):
    genes = []

    for g in range(GENES):
        genes.append(randint(0, STRATEGIES-1))
    
    chromosomes.append(genes)

def lowest_weight(connections_subset_list):
  lowest_weight = MAX_WEIGHT

  for connection in connections_subset_list:
    if connection[2] < lowest_weight:
      lowest_weight = connection[2]
      lowest_connection = connection

  return lowest_connection

def random_weight(connections_subset_list):
  r = randint(0, len(connections_subset_list)-1)

  random_connection = connections_subset_list[r]

  return random_connection


def first_weight(connections_subset_list):
  return connections_subset_list[0]


def highest_weight(connections_subset_list):
  highest_weight = 0

  for connection in connections_subset_list:
    if connection[2] > highest_weight:
      highest_weight = connection[2]
      highest_connection = connection

  return highest_connection

def evolve():
    for generation in range(GENERATIONS):
        cdf = []
        cdf_total = 0
        scores = []

        for i, chromosome in enumerate(chromosomes):
            visited_list = []
            curr_node = 'a'
            visited_list.append('a')
            weight_score = 0

            for gene in chromosome:
                connections_subset_list = []
    
                for connection in graph['connections']:
                    if connection[0] == curr_node or connection[1] == curr_node:
                        if not (connection[0] in visited_list and connection[1] in visited_list):
                            connections_subset_list.append(connection)
    
                if len(connections_subset_list) > 0:
                    if gene == 0:
                        choosen_connection = lowest_weight(connections_subset_list)
                    elif gene == 1:
                        choosen_connection = random_weight(connections_subset_list)
                    elif gene == 2:
                        choosen_connection = first_weight(connections_subset_list)
                    elif gene == 3:
                        choosen_connection = highest_weight(connections_subset_list)          
                    else: 
                        print('no strategy')
                        break

                    if choosen_connection[0] == curr_node:
                        connected_node = choosen_connection[1]
                    elif choosen_connection[1] == curr_node:
                        connected_node = choosen_connection[0]
                    
                    visited_list.append(connected_node)
                    curr_node = connected_node

                    weight_score = weight_score + choosen_connection[2]
                else:
                    continue

            weight_score_pct = Decimal(weight_score) / Decimal(100)
            node_score = len(visited_list)
            score = Decimal(node_score) - Decimal(weight_score_pct)
            scores.append(score)
            cdf_total = cdf_total + score
            cdf.append(cdf_total)

        crossover(cdf, cdf_total, scores)
        mutate()
        replace_old_population()

def crossover(cdf, cdf_total, scores):
    global chromosomes
    global offsprings

    for i in range(CHROMOSOMES):
        parent_1_index = 0
        parent_2_index = 0

        r1 = Decimal(random())
        random_number_1 = r1 * Decimal(cdf_total)

        for j in range(CHROMOSOMES):
            # -1 - if a < b, 0 - if a == b
            if random_number_1.compare(cdf[j]) < 1:
                parent_1_index = j
                break

        r2 = Decimal(random())
        random_number_2 = r2 * cdf_total

        for j in range(CHROMOSOMES):
            if random_number_2.compare(cdf[j]) < 1:
                parent_2_index = j
                break

        cut_point = randint(1, GENES-1)  # 0|1|0|0|1

        offspring = chromosomes[parent_1_index][:cut_point] + chromosomes[parent_2_index][cut_point:]
        offsprings.append(offspring)

def mutate():
    global offsprings

    for i in range(CHROMOSOMES):
        for j in range(GENES):
            r1 = Decimal(random())
            if r1.compare(MUTATION_RATE) == -1:
                offsprings[i][j] ^= 1

def replace_old_population():
    global chromosomes
    global offsprings

    chromosomes = offsprings.copy()

evolve()        



