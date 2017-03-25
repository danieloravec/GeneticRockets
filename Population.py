import random
import math
from DNA import DNA
from Constants import Constants


class Population:
    def __init__(self, _visualiser, _population_size, _mutation_rate, _target_x, _target_y, _target_diameter, _target_color,
                 _rocket_height, _rocket_width, _rocket_color, _genes_amount):
        self.visualiser = _visualiser
        self.generation = 0
        self.population_size = _population_size
        # Mutation rate in [%]
        self.mutation_rate = _mutation_rate
        self.target_x = _target_x
        self.target_y = _target_y
        self.target_diameter = _target_diameter
        self.target = [[self.target_x, self.target_y], self.target_diameter]
        self.mating_pool = []
        self.population = []
        self.x = 0
        self.y = 0
        for _ in range(self.population_size):
            self.population.append(DNA(_genes_amount, self.target_x, self.target_y, self.target_diameter, self.population_size,
                                       _rocket_height, _rocket_width, _rocket_color))

    def calculate_fitness(self):
        for i in range(len(self.population)):
            self.population[i].calculate_fitness()

    def run_fitness_test(self):
        for i in range(len(self.population)):
            for j in range(len(self.population[i].genes)):
                self.population[i].rocket.x += self.population[i].genes[j].x_movement
                self.population[i].rocket.y += self.population[i].genes[j].y_movement
                self.visualiser.redraw_situation(self.population[i].rocket, i)
                x_distance = abs(self.population[i].rocket.x - self.target_x)
                y_distance = abs(self.population[i].rocket.y - self.target_y)
                act_distance = int(math.ceil(math.sqrt(x_distance ** 2 + y_distance ** 2)))
                self.population[i].min_distance_to_target\
                    = min(self.population[i].min_distance_to_target, act_distance)
                self.population[i].fitness\
                    = max(self.population[i].fitness,
                          Constants.max_distance - self.population[i].min_distance_to_target)

    def natural_selection(self):
        max_fitness = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > max_fitness:
                max_fitness = self.population[i].fitness
        self.mating_pool = []
        for i in range(len(self.population)):
            safe_counter = 0
            while True:
                safe_counter += 1
                random_number = random.randint(0, max_fitness)
                random_index = random.randint(0, len(self.population) - 1)
                # If something goes wrong, pick random element from population and then exit
                if random_number < max_fitness / 2 or safe_counter > 100:
                    self.mating_pool.append(self.population[random_index])
                    break
                elif safe_counter > 100:
                    break

    def next_generation(self):
        for i in range(len(self.population)):
            random_a = random.randint(0, len(self.population) - 1)
            random_b = random.randint(0, len(self.population) - 1)
            parent_a = self.mating_pool[random_a]
            parent_b = self.mating_pool[random_b]
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generation += 1
