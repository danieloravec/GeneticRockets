import random
from DNA import DNA


class Population:
    def __init__(self, _population_size, _mutation_rate, _target):
        self.generation = 0
        self.population_size = _population_size
        # Mutation rate in [%]
        self.mutation_rate = _mutation_rate
        self.target = _target
        self.mating_pool = []
        self.population = []
        for _ in range(self.population_size):
            self.population.append(DNA(self.target))

    def calculate_fitness(self):
        for i in range(len(self.population)):
            self.population[i].calculate_fitness()

    def natural_selection(self):
        max_fitness = 0
        max_fitness_index = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > max_fitness:
                max_fitness = self.population[i].fitness
                max_fitness_index = i
        print("GENERATION: " + str(self.generation))
        print("Best string: " + str(self.population[max_fitness_index].genes))
        print()
        self.mating_pool = []
        for i in range(len(self.population)):
            for j in range(self.population[i].fitness):
                self.mating_pool.append(self.population[i])

    def next_generation(self):
        for i in range(len(self.population)):
            random_a = random.randint(0, len(self.mating_pool) - 1)
            random_b = random.randint(0, len(self.mating_pool) - 1)
            parent_a = self.mating_pool[random_a]
            parent_b = self.mating_pool[random_b]
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generation += 1

    def is_finished(self):
        for i in range(len(self.population)):
            ok = True
            for j in range(len(self.target)):
                if self.population[i].genes[j] != self.target[j]:
                    ok = False
                    break
            if ok:
                return True
        return False
