import pygame

class Pipe:
    def __init__(self, gap, height, windWidth, windHeight):
        self.height = height
        self.width = 60

        self.windWidth = 1200
        self.windHeight = 700

        self.delay = 50
        self.gap = gap
        self.posX = self.windWidth + self.gap#self.delay

        self.color = (0, 255, 0)

        self.speed = 300

    def update(self, dt):
        self.posX -= self.speed * dt

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.posX, 0, self.width, self.windHeight))
