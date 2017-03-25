try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from Init import Init


class Visualiser:
    def __init__(self, _canvas_width, _canvas_height, _max_population, _mutation_rate,
                 _target_x, _target_y, _target_diameter, _target_color,
                 _background_color, _rocket_height, _rocket_width, _rocket_color, _genes_amount):
        self.canvas_width = _canvas_width
        self.canvas_height = _canvas_height
        self.target_x = _target_x
        self.target_y = _target_y
        self.target_diameter = _target_diameter
        self.target_color = _target_color
        self.background_color = _background_color
        self.drawn_rockets = []
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.canvas_width, heigh=self.canvas_height)
        self.canvas.pack()
        self.text = self.canvas.create_text(5, self.canvas_height - 20, text='Nan')
        # Main part to be visualised
        self.evolution = Init(self, _max_population, _mutation_rate, _target_x, _target_y, _target_diameter,
                              _target_color, _rocket_height, _rocket_width, _rocket_color, _genes_amount)

    def redraw_situation(self, rocket_to_redraw, rocket_index):
        self.canvas.delete(self.drawn_rockets[rocket_index])
        new_rocket = self.canvas.create_rectangle(rocket_to_redraw.x, rocket_to_redraw.y,
                                                  rocket_to_redraw.x + rocket_to_redraw.width,
                                                  rocket_to_redraw.y + rocket_to_redraw.height,
                                                  fill=rocket_to_redraw.color)
        self.drawn_rockets[rocket_index] = new_rocket
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(50, self.canvas_height - 30,
                                            text='Generation: ' + str(self.evolution.population.generation))

    def draw_initial(self):
        self.canvas.configure(background=self.background_color)
        for dna in self.evolution.population.population:
            new_rocket = self.canvas.create_rectangle(dna.rocket.x, dna.rocket.y,
                                                      dna.rocket.x + dna.rocket.width, dna.rocket.y + dna.rocket.height,
                                                      fill=self.evolution.population.population[0].rocket.color)
            self.drawn_rockets.append(new_rocket)
        self.canvas.create_oval(self.target_x, self.target_y, self.target_x + self.target_diameter,
                                self.target_y + self.target_diameter, fill=self.target_color)


