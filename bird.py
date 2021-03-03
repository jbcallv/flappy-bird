import pygame

class Bird:
    def __init__(self):
        # pos = tuple
        self.pos = [400, 300]
        self.size = 40
        self.color = (255, 255, 0)
        self.speed = 400
        self.gravity = -200

        self.windWidth = 1200
        self.windHeight = 700
        self.acceleration = 0.1

        self.acceleration2 = 0.1

    def flap(self, dt):
        if (self.pos[1] >= 0):
            self.pos[1] -= self.speed * dt * self.acceleration
            self.acceleration += 0.1

        else:
            self.acceleration = 0.1

        if (self.acceleration >= 1):
            if (self.acceleration >= 0.1):
                self.acceleration -= 0.3


    def update(self, dt, flapped):
        #self.flap(dt)
        if ((self.pos[1] + self.size) <= self.windHeight):
            self.pos[1] -= self.gravity * dt * self.acceleration2
            self.acceleration2 += 0.1
        
        # acceleration
        else:
            self.acceleration2 = 0.1

        if (self.acceleration2 >= 2):
            if (self.acceleration2 >= 0.1):
                self.acceleration2 -= 0.2

        if (flapped):
            for i in range(20):
                self.flap(dt)

    def draw(self, window):
        #window.fill((0, 0, 0))
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))
