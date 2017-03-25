from Population import Population
from Target import Target


class Init:
    def __init__(self, _visualiser, _population_size, _mutation_rate, _target_x, _target_y, _target_diameter,
                 _target_color, _rocket_height, _rocket_width, _rocket_color, _genes_amount):
        self.population_size = _population_size
        self.mutation_rate = _mutation_rate
        self.visualiser = _visualiser
        self.target = Target(_target_x, _target_y, _target_diameter, _target_color)
        self.population = Population(self.visualiser, self.population_size, self.mutation_rate,
                                     _target_x, _target_y, _target_diameter, _target_color,
                                     _rocket_height, _rocket_width, _rocket_color, _genes_amount)

    def evolve(self):
        self.population.run_fitness_test()
        self.population.natural_selection()
        self.population.next_generation()
