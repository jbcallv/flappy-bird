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

# game has started
started = False

while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = game.quit()

        if (event.type == pygame.KEYDOWN):
            # quit
            if (event.key == pygame.K_ESCAPE):
                running = game.quit()

            # flap
            if (event.key == pygame.K_SPACE):
                if (started):
                    flapped = True

            # restart
            if (event.key == pygame.K_r):
                game.restart()

            # start game
            if (event.key == pygame.K_s):
                if (game.can_start):
                    started = game.start_game()

    # always draw and clear screen
    screen.fill((0, 0, 0))
    game.draw()

    # only call if game has been started
    if (started):
        dt = clock.tick(60) * 0.001
        game.update(dt, flapped)
        flapped = False


    # update screen
    pygame.display.update()
