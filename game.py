# randomness and pygame
import pygame
import random

# bird, pipes, and text
from bird import Bird
from pipe import Pipe
from text import Text

# handles game logic
class Game:
    def __init__(self, window):

        # get the window and an array of pipes on the screen
        self.window = window
        self.pipe_array = []

        # score stuff
        self.incremented = False
        self.score = 0

        # text stuff
        self.text = Text(self.window)
        self.text.start_text()
        self.bird = Bird()

        # you can only 'start' the game once: at the beginning
        self.can_start = True

    def start_game(self):
        # start the game
        if (self.can_start):
            self.text.reset_text()
            self.bird = Bird()
            self.generate_pipes()
            self.timer = 0
            self.collided = False
            self.can_start = False
            return True

    def generate_pipes(self):
        # generate the pipes with a delay of (param1) and (param for pipe 2)
        p1 = Pipe(300)
        p2 = Pipe(300 + 480)

        self.pipe_array.append(p1)
        self.pipe_array.append(p2)

    def check_collision(self):
        for pipe in self.pipe_array:
            # check if bottom of bird has collided
            if ((self.bird.pos[1] + self.bird.size) >= (pipe.rand + pipe.gapSize) and self.bird.pos[0] > pipe.posX and self.bird.pos[0] < (pipe.posX + pipe.width)):
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            # check if top of bird has collided
            if (self.bird.pos[1] <= (pipe.rand) and self.bird.pos[0] > pipe.posX and self.bird.pos[0] < (pipe.posX + pipe.width)):
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            # check if right of bird has collided
            if ((self.bird.pos[0] + self.bird.size) >= pipe.posX and (self.bird.pos[0] + self.bird.size) <= (pipe.posX + pipe.width) and self.bird.pos[1] < pipe.rand or (self.bird.pos[0] + self.bird.size) >= pipe.posX and (self.bird.pos[0] + self.bird.size) <= (pipe.posX + pipe.width) and self.bird.pos[1] > (pipe.rand + pipe.gapSize)):
                # collide
                self.collided = True
                self.text.restart_text()
                return True

            else:
                # no collisions
                self.collided = False
                return False

    def track_score(self):
        # increment score once when bird passes through pipe
        for pipe in self.pipe_array:
            if (self.incremented == False):
                if (self.bird.pos[1] >= (pipe.rand) and (self.bird.pos[1] + self.bird.size) <= (pipe.rand + pipe.gapSize) and self.bird.pos[0] > pipe.posX and self.bird.pos[0] < (pipe.posX + pipe.width)):
                    self.score += 1
                    self.text.set_score(self.score)
                    self.incremented = True

            if (self.bird.pos[0] > (pipe.posX + pipe.width)):
                self.incremented = False


    def quit(self):
        # quit the game
        return False

    def restart(self):
        # restart game by resetting all variables
        if (self.collided == True):
            self.score = 0
            self.text = Text(self.window)
            self.bird = Bird()
            self.pipe_array.clear()
            self.timer = 0
            self.generate_pipes()

    def update(self, dt, flapped):
        # as long as there are no collisions
        if (self.check_collision() == False):
            # handle the game logic updates
            self.track_score()
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
        # draw everything
        self.bird.draw(self.window)

        for pipe in self.pipe_array:
            pipe.draw(self.window)
            
        self.text.draw()
