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
STRATEGIES = 4

for i in range(CHROMOSOMES):
    genes = []

    for g in range(GENES):
        genes.append(randint(0, STRATEGIES-1))
    
    chromosomes.append(genes)

print(chromosomes)

