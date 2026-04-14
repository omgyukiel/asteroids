from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True

    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
