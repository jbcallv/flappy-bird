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

        self.timer = 0

    def generate_pipes(self):
        gap = random.randint(300, 600)
        gap1 = random.randint(300, 600)

        p1 = Pipe(300)
        p2 = Pipe(300 + 480)

        self.pipe_array.append(p1)
        self.pipe_array.append(p2)

    def quit(self):
        pass

    def update(self, dt, flapped):
        self.timer += 1

        if (self.timer >= 200):
            self.generate_pipes()
            self.timer = 0

        self.bird.update(dt, flapped)
        for pipe in self.pipe_array:
            if (pipe.posX + pipe.width > 0):
                pipe.update(dt)
            else:
                self.pipe_array.remove(pipe)

    def draw(self):
        self.bird.draw(self.window)

        for pipe in self.pipe_array:
            pipe.draw(self.window)
