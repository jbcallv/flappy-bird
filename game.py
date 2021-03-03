import pygame
import random

from bird import Bird
from pipe import Pipe

# handles game logic
class Game:
    def __init__(self, window):
        #self.pipe = Pipe(60, 1200, 700)

        self.bird = Bird()
        self.window = window
        self.pipe_array = []

        #self.pipe_array.append(self.pipe)
        self.generate_pipes()

    def generate_pipes(self):
        h1 = random.randint(0, 50)
        h2 = random.randint(0, 50)

        gap = random.randint(200, 300)

        p1 = Pipe(60, h1, 1200, 700)
        p2 = Pipe(60 + gap, h2, 1200, 700)

        self.pipe_array.append(p1)
        self.pipe_array.append(p2)

    def quit(self):
        pass

    def update(self, dt, flapped):
        self.bird.update(dt, flapped)
        for pipe in self.pipe_array:
            pipe.update(dt)

    def draw(self):
        self.bird.draw(self.window)

        for pipe in self.pipe_array:
            pipe.draw(self.window)
