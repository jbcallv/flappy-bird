import pygame
import random

# handles pipes
class Pipe:
    def __init__(self, gap):
        # default pipe width
        self.width = 60

        # window width and height
        self.windWidth = 1200
        self.windHeight = 700

        # delay between pipes appearing on screen
        self.gap = gap
        self.posX = self.windWidth + self.gap

        # pipe color
        self.color = (0, 255, 0)

        # pipe movement speed
        self.speed = 300

        # size of gaps between top and bottom pipes
        self.gapSize = random.randint(185, 300)

        # the height of the top pipe
        self.rand = random.randint(100, 400)

    def update(self, dt):
        # change the pipe position on each frame
        self.posX -= self.speed * dt

    def draw(self, window):
        # draw the top and bottom pipes
        pygame.draw.rect(window, self.color, pygame.Rect(self.posX, 0, self.width, self.rand))
        pygame.draw.rect(window, self.color, pygame.Rect(self.posX, self.rand + self.gapSize, self.width, self.windHeight))
