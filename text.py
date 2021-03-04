import pygame

pygame.font.init()

class Text:
    def __init__(self, window):
        self.window = window

        self.restart = False
        self.start = False

        self.big_size = 50
        self.normal_size = 30
        
        self.big_font = pygame.font.SysFont('freesansbold.ttf', self.big_size)
        self.normal_font = pygame.font.SysFont('freesansbold.ttf', self.normal_size)
        self.score_font = pygame.font.SysFont('freesansbold.ttf', self.normal_size)

        # score
        self.score = 0

        # text to be drawn
        self.big_text = ""
        self.text = ""
        self.score_text = str(self.score)

    def start_text(self):
        self.big_text = "Flappy Bird"
        self.text = "Press 's' key to start game" 

    def reset_text(self):
        self.big_text = ""
        self.text = ""

    def restart_text(self):
        self.big_text = "You lost!"
        self.text = "Press 'r' key to restart game"

    def set_score(self, score):
        self.score = score
        self.score_text = str(score)

    def update(self, dt):
        self.draw()

    def draw(self):
        big_surface = self.big_font.render(self.big_text, 1,  (255, 255, 255), (0, 0, 0))
        normal_surface = self.normal_font.render(self.text, 1, (255, 255, 255), (0, 0, 0))
        score_surface = self.score_font.render("Score: " + self.score_text, 1, (255, 255, 255), (0, 0, 0))

        self.window.blit(big_surface, (500, 185))
        self.window.blit(normal_surface, (475, 240))
        self.window.blit(score_surface, (0, 0))
