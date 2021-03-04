import pygame

class Text:
    def __init__(self):
        self.restart = False
        self.start = False

        self.big_size = 20
        self.normal_size = 12
        
        big_font = pygame.font.SysFont('freesansbold.ttf', self.big_size)
        normal_font = pygame.font.SysFont('freesansbold.ttf', self.normal_size)

        # text to be drawn
        self.big_text = ""
        self.text = ""
        self.score_text = ""

    def start_text(self):
        self.big_text = "Flappy Bird"
        self.text = "Press 's' key to start game" 

    def restart_text(self):
        self.big_text = "You lost!"
        self.text = "Press 'r' key to restart game"

    def set_score(self, score):
        self.score_text = str(score)

    def update(self, dt):
        pass

    def draw(self):
        pass
