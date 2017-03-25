import random


class Vector:
    def __init__(self, _x_movement, _y_movement, _max_unit_length):
        self.x_movement = _x_movement
        self.y_movement = _y_movement
        self.max_unit_length = _max_unit_length


def get_random_vector(max_unit_length):
    random_x_movement = random.randint(-max_unit_length, max_unit_length)
    random_y_movement = random.randint(-max_unit_length, max_unit_length)
    new_random_vector = Vector(random_x_movement, random_y_movement, max_unit_length)
    return new_random_vector
