from Population import Population


class Init:
    def __init__(self, _population_size, _mutation_rate, _target):
        self.population_size = _population_size
        self.mutation_rate = _mutation_rate
        self.target = _target
        self.population = Population(self.population_size, self.mutation_rate, self.target)

    def evolve(self):
        while not(self.population.is_finished()):
            self.population.calculate_fitness()
            self.population.natural_selection()
            self.population.next_generation()
        print("Evolved to " + str(self.target) + " in generation " + str(self.population.generation))
