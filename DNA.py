import random


class DNA:
    def __init__(self, _target):
        self.target = _target
        self.fitness = 0
        self.genes = self.generate_genes()

    def generate_genes(self):
        new_genes = []
        for i in range(len(self.target)):
            random_character = self.get_char()
            new_genes.append(random_character)
        return new_genes

    def calculate_fitness(self):
        self.fitness = 0
        for i in range(len(self.target)):
            if self.genes[i] == self.target[i]:
                self.fitness += 1

    def crossover(self, second_parent):
        child = DNA(self.target)
        child.genes = []
        midpoint = random.randint(0, len(self.target))
        for i in range(midpoint):
            child.genes.append(self.genes[i])
        for i in range(midpoint, len(self.genes)):
            child.genes.append(second_parent.genes[i])
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            random_number = random.randint(1, 101)
            if random_number <= mutation_rate:
                self.genes[i] = self.get_char()

    def get_char(self):
        random_ascii = random.randint(32, 123)
        return chr(random_ascii)
