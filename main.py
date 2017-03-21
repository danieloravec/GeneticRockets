from Visualiser import Visualiser
import time

max_population = 10  # input("Population size: ")
mutation_rate = 1  # input("Mutation rate: ")
canvas_width = 800
canvas_height = 600
target_x = 500
target_y = 500
target_diameter = 100
target_color = 'blue'
background_color = 'green'
rocket_height = 50
rocket_width = 20
rocket_color = 'orange'
visualisation =\
    Visualiser(canvas_width, canvas_height, max_population, mutation_rate, target_x, target_y, target_diameter,
               target_color, background_color, rocket_height, rocket_width, rocket_color)

if __name__ == "__main__":
    visualisation.redraw_situation()
    visualisation.evolution.evolve()
    time.sleep(0.5)
    visualisation.root.mainloop()
