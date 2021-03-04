import pygame
from game import Game

# default screen size
WIDTH = 1200
HEIGHT = 700

# game screen window tuple
size = (WIDTH, HEIGHT)

# set the game window size and caption
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

# game logic
# potentially pass in level
game = Game(screen)

# create the game window
pygame.display.flip()

# game loop
running = True

# time
clock = pygame.time.Clock()
dt = 0

flapped = False

while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = game.quit()

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                running = game.quit()

            if (event.key == pygame.K_SPACE):
                flapped = True

            if (event.key == pygame.K_r):
                game.restart()

    screen.fill((0, 0, 0))
    dt = clock.tick(60) * 0.001
    print(dt)
    game.update(dt, flapped)
    flapped = False
    game.draw()

    pygame.display.update()
