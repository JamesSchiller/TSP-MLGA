from random import randint
from random import random
from decimal import *
import json

global REPORT
global GENERATIONS
global MUTATION_RATE
global organisms
global offspring
global cdfs
global scores
global cdfsum

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

REPORT = True
ORGANISMS = 100
GENES = len(graph['connections'])
GENERATIONS = 300
MUTATION_RATE = 0.05

organisms = []
for o in range(ORGANISMS):
  genes = []
  for g in range(GENES):
    genes.append([0])
  organisms.append(genes)

offspring = []
for o in range(ORGANISMS):
  for g in range(GENES):
    genes.append([0])
  offspring.append(genes)

for o in range(ORGANISMS):
  for g in range(GENES):
    organisms[o][g] = randint(0, 3)

scores = [ 0 for i in enumerate(organisms) ]
cdfsum = 0
cdfs = [ 0 for i in enumerate(organisms) ]

if REPORT:
  file = open('report.txt', 'w')
  file.write('graph\n')
  file.write('-----------------\n')
  for connection in graph['connections']:
    file.write(str(connection) + '\n')
  # file.write(json.dumps(graph['connections']) + '\n')
  file.write('-----------------\n')
  file.write('parameters\n')
  file.write('-----------------\n')
  file.write('ORGANISMS: ' + str(ORGANISMS)  + '\n')
  file.write('GENES: ' + str(GENES) + '\n')
  file.write('GENERATIONS: ' + str(GENERATIONS) + '\n')
  file.write('MUTATION_RATE: ' + str(MUTATION_RATE) + '\n')
  file.write('-----------------\n')
  file.write('initial organisms\n')
  file.write('-----------------\n')
  for organism in organisms:
    file.write(str(organism) + '\n')

def lowest_weight(connections_subset_list):
  lowest_weight = 10
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

def think():
  global scores
  global cdfs
  global cdfsum

  for generation in range(GENERATIONS):

    for o, organism in enumerate(organisms):
      curr_node = 'a'
      node_score = 0
      weight_score = 0
      visited_list = []
      visited_list.append('a')

      for gene in organism:
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
          node_score = len(visited_list)
          weight_score = weight_score + choosen_connection[2]
        else:
          continue

      weight_score_pct = Decimal(weight_score) / Decimal(100) 
      scores[o] = (node_score - weight_score_pct)      
      cdfsum = cdfsum + scores[o]
      cdfs[o] = cdfsum 
    
    if generation < GENERATIONS-1: 
      reproduce(cdfs, cdfsum)
      replace_old_population()

      scores = [ 0 for i in enumerate(organisms) ]
      cdfsum = 0
      cdfs = [ 0 for i in enumerate(organisms) ]

    if REPORT: 
      file.write('generation: ' + str(generation) + '\n')
      
      for organism in organisms: 
        file.write(str(organism) + '\n')

def do(organism):
  curr_node = 'a'
  node_score = 0
  weight_score = 0
  visited_list = []
  visited_list.append('a')
  
  for gene in organism:
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

  node_score = len(visited_list)

  if REPORT:
    file.write('-----------------\n')
    file.write('best organism\n')
    file.write('-----------------\n')
    file.write('organism: ' + str(organism) + '\n')
    file.write('visited: ' + str(visited_list) + '\n')
    file.write('node_score: ' + str(node_score) + '\n')
    file.write('weight_score: ' + str(weight_score) + '\n')
    file.close()

  print('best organism')
  print('-----------------')
  print('organism: ' + str(organism))
  print('visited: ' + str(visited_list))
  print('node_score: ' + str(node_score))
  print('weight_score: ' + str(weight_score))

def crossover(parent1index, parent2index, childindex):
    global organisms 

    cutpoint = randint(1, GENES-1)
    offspring[childindex] = organisms[parent1index][:cutpoint] + organisms[parent2index][cutpoint:]

def mutate(childindex):
    global offspring

    for i, gene in enumerate(offspring[childindex]):
      if random() < MUTATION_RATE: 
        offspring[childindex][i] = randint(0, 3)
    
def replace_old_population():
    global organisms
    global offspring

    organisms = offspring.copy()

def reproduce(cdfs, cdfsum): 
    global organisms

    for childindex in range(ORGANISMS):
        random_number = Decimal(str(random())) * cdfsum
        
        for o in range(ORGANISMS):
            if random_number <= cdfs[o]:
                parent1index = o
                break

        random_number = Decimal(str(random())) * cdfsum

        for o in range(ORGANISMS):
            if random_number <= cdfs[o]:
                parent2index = o
                break

        crossover(parent1index, parent2index, childindex)
        mutate(childindex)

def save_highest_organism():
    highest_rated_index = 0

    for o in range(ORGANISMS):
        if scores[o] > scores[highest_rated_index]:
            highest_rated_index = o
    
    organism, organism_score = save_organism(highest_rated_index)

    return organism, organism_score

def save_organism(o): 
    organism = organisms[o]
    organism_score = scores[o]

    return organism, organism_score

think()
organism, organism_score = save_highest_organism()

do(organism)