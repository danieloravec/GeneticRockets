from Init import Init


if __name__ == "__main__":
    # max_population = input("Population size: ")
    # mutation_rate = input("Mutation rate: ")
    # target = input("Target phrase: ")
    max_population = 1000
    mutation_rate = 1
    target = "To be or not to be."
    evolution = Init(max_population, mutation_rate, target)
    evolution.evolve()
