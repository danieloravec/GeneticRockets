try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from Init import Init


class Visualiser:
    def __init__(self, _canvas_width, _canvas_height, _max_population, _mutation_rate,
                 _target_x, _target_y, _target_diameter, _target_color,
                 _background_color, _rocket_height, _rocket_width, _rocket_color):
        self.canvas_width = _canvas_width
        self.canvas_height = _canvas_height
        self.target_x = _target_x
        self.target_y = _target_y
        self.target_diameter = _target_diameter
        self.target_color = _target_color
        self.background_color = _background_color
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.canvas_width, heigh=self.canvas_height)
        self.canvas.pack()
        # Main part to be visualised
        self.evolution = Init(_max_population, _mutation_rate, _target_x, _target_y, _target_diameter, _target_color,
                              _rocket_height, _rocket_width, _rocket_color)

    def redraw_situation(self):
        self.canvas.delete('all')
        self.canvas.configure(background=self.background_color)
        for dna in self.evolution.population.population:
            self.canvas.create_rectangle(dna.rocket.x, dna.rocket.y,
                                         dna.rocket.x + dna.rocket.width, dna.rocket.y + dna.rocket.height,
                                         fill=self.evolution.population.population[0].rocket.color)
        self.canvas.create_oval(self.target_x, self.target_y, self.target_x + self.target_diameter,
                                self.target_y + self.target_diameter, fill=self.target_color)

