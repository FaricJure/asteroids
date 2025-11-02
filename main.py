# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
