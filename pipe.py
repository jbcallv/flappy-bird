import pygame
import random

class Pipe:
    def __init__(self, gap):
        #self.height = height
        self.width = 60

        self.windWidth = 1200
        self.windHeight = 700

        self.delay = 50
        self.gap = gap
        self.posX = self.windWidth + self.gap#self.delay

        self.color = (0, 255, 0)

        self.speed = 300

        self.gapSize = 300

        self.rand = random.randint(100, 400)

    def update(self, dt):
        self.posX -= self.speed * dt

    def draw(self, window):
        #rand = random.randint(100, 400)
        pygame.draw.rect(window, self.color, pygame.Rect(self.posX, 0, self.width, self.rand))
        pygame.draw.rect(window, self.color, pygame.Rect(self.posX, self.rand + self.gapSize, self.width, self.windHeight))
