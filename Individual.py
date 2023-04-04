import random


class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome, target, genes, lookup):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness(target, lookup)
        self.genes = genes
        self.target = target
        self.lookup = lookup

    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        gene = random.choice(self.genes)
        return gene

    @classmethod
    def create_gnome(self, size):
        '''
        create chromosome or string of genes
        '''
        gnome = []
        for i in range(size):
            gnome.append("{0}".format(round(random.randint(0, 1))))
        return gnome

    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        child = Individual.create_gnome(len(self.lookup.keys()))
        return Individual(child, self.target, self.genes, self.lookup)

    def cal_fitness(self, target, lookup):
        weight = 0
        score = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == "1":
                option_label = list(lookup.keys())[i]
                obj_on = lookup[option_label]
                weight += obj_on[0]
                score += obj_on[1]
            if weight > target:
                score = -1
        return score
