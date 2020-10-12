def print_chromosomes(chromosomes):
    for chromosome in chromosomes:
        print(chromosome)

def write_chromosomes(file, chromosomes):
    for chromosome in chromosomes:
        file.write(str(chromosome) + '\n')