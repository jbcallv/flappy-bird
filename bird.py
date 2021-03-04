import pygame

# handles bird
class Bird:
    def __init__(self):
        # bird's x and y position
        self.pos = [400, 300]
        # height and width of bird
        self.size = 40
        self.color = (255, 255, 0)

        # bird speed, pull of gravity, and acceleration
        self.speed = 400
        self.gravity = -200
        self.acceleration = 0.1
        self.acceleration2 = 0.1

        # window width and height
        self.windWidth = 1200
        self.windHeight = 700
        
    def flap(self, dt):
        # makes the bird move up
        if (self.pos[1] >= 0):
            # only flap if you are below top of screen
            self.pos[1] -= self.speed * dt * self.acceleration
            # cheesy linear interpolation
            self.acceleration += 0.1

        else:
            self.acceleration = 0.1

        # cheesy linear interpolation
        if (self.acceleration >= 1):
            if (self.acceleration >= 0.1):
                self.acceleration -= 0.3


    def update(self, dt, flapped):
        # constant pull of gravity
        if ((self.pos[1] + self.size) <= self.windHeight):
            self.pos[1] -= self.gravity * dt * self.acceleration2
            # cheesy linear interpolation
            self.acceleration2 += 0.1
        
        # cheesy linear interpolation
        else:
            self.acceleration2 = 0.1

        if (self.acceleration2 >= 2):
            if (self.acceleration2 >= 0.1):
                self.acceleration2 -= 0.2

        # cheesy linear interpolation
        if (flapped):
            # flap 20 times as acceleration changes (cheesy lerp)
            for i in range(20):
                self.flap(dt)

    def draw(self, window):
        # draws bird
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))
