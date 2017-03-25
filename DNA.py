import random
import Vector
from Constants import Constants
from Rocket import Rocket


class DNA:
    def __init__(self, _target_x, _target_y, _target_diameter, _population_size,
                 _rocket_height, _rocket_width, _rocket_color):
        self.target_x = _target_x
        self.target_y = _target_y
        self.target_diameter = _target_diameter
        self.population_size = _population_size
        self.fitness = 0
        self.rocket = Rocket(0, 0, _rocket_height, _rocket_width, _rocket_color)
        self.min_distance_to_target = Constants.infinity
        self.genes = []
        self.generate_genes()

    def generate_genes(self):
        self.genes = []
        for _ in range(self.population_size):
            y_movement = random.randint(-self.target_diameter, self.target_diameter)
            x_movement = random.randint(-self.target_diameter, self.target_diameter)
            new_vector = Vector.Vector(x_movement, y_movement, self.target_diameter)
            self.genes.append(new_vector)

    def calculate_fitness(self):
        self.fitness = Constants.max_distance - self.min_distance_to_target

    def crossover(self, second_parent):
        child = DNA(self.target_x, self.target_y, self.target_diameter, self.population_size,
                    self.rocket.height, self.rocket.width, self.rocket.color)
        child.genes = []
        midpoint = random.randint(0, len(self.genes))
        for i in range(midpoint):
            child.genes.append(self.genes[i])
        for i in range(midpoint, len(self.genes)):
            child.genes.append(second_parent.genes[i])
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            random_number = random.randint(1, 100)
            if random_number <= mutation_rate:
                self.genes[i] = Vector.get_random_vector(self.target_diameter)
