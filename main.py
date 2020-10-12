from random import randint

global graph

chromosomes = []

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

CHROMOSOMES = 2
GENES = len(graph['connections'])
GENERATIONS = 4
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
        payoffs = []

        for chromosome in chromosomes:
            visited_list = []
            curr_node = 'a'
            visited_list.append('a')

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

                    # todo: weights = scores or payoff or ...
                    
                    # node_score = len(visited_list)
                    # weight_score = weight_score + choosen_connection[2]
                else:
                    continue

            # weight_score_pct = Decimal(weight_score) / Decimal(100) 
            # scores[o] = Decimal(node_score) - Decimal(weight_score_pct))      
            # cdf_total = cdf_total + scores[o]
            # cdfs[o] = cdfsum 

            # crossover(cdf, cdf_total, payoffs)
            # mutate()
            # replace_old_population()

evolve()        



