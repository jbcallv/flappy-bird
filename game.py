import pygame
import random

from bird import Bird
from pipe import Pipe
from text import Text

# handles game logic
class Game:
    def __init__(self, window):
        #self.start_game()

        #self.bird = Bird()
        self.window = window
        self.pipe_array = []
        #self.start_game()

        #self.generate_pipes()

        #self.timer = 0

        # flag to check collisions
        #self.collided = False

        self.text = Text(self.window)
        self.text.start_text()
        self.bird = Bird()

        self.can_start = True

    def start_game(self):
        if (self.can_start):
            #self.text = Text(self.window)
            #self.text.start_text()
            self.text.reset_text()
            self.bird = Bird()
            self.generate_pipes()
            self.timer = 0
            self.collided = False
            self.can_start = False
            return True

    def generate_pipes(self):
        gap = random.randint(300, 600)
        gap1 = random.randint(300, 600)

        p1 = Pipe(300)
        p2 = Pipe(300 + 480)

        self.pipe_array.append(p1)
        self.pipe_array.append(p2)

    def check_collision(self):
        for pipe in self.pipe_array:
            # check if bottom of bird has collided
            if ((self.bird.pos[1] + self.bird.size) >= (pipe.rand + pipe.gapSize) and self.bird.pos[0] > pipe.posX and self.bird.pos[0] < (pipe.posX + pipe.width)):
                print("bottom collision")
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            # check if top of bird has collided
            if (self.bird.pos[1] <= (pipe.rand) and self.bird.pos[0] > pipe.posX and self.bird.pos[0] < (pipe.posX + pipe.width)):
                print("top collision")
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            # check if right of bird has collided
            if ((self.bird.pos[0] + self.bird.size) >= pipe.posX and (self.bird.pos[0] + self.bird.size) <= (pipe.posX + pipe.width) and self.bird.pos[1] < pipe.rand or (self.bird.pos[0] + self.bird.size) >= pipe.posX and (self.bird.pos[0] + self.bird.size) <= (pipe.posX + pipe.width) and self.bird.pos[1] > (pipe.rand + pipe.gapSize)):
                print("right collision")
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            else:
                # no collisions
                self.collided = False
                return False

    def quit(self):
        return False

    def restart(self):
        if (self.collided == True):
            self.text = Text(self.window)
            self.bird = Bird()
            self.pipe_array.clear()
            self.timer = 0
            self.generate_pipes()

    def update(self, dt, flapped):
        print(self.check_collision())
        if (self.check_collision() == False):
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
            
        self.text.draw()
