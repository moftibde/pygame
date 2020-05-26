import pygame
from pygame.locals import (
    KEYDOWN,
    K_SPACE,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT,
)
from time import time
from python.pygame.Game_3.details import ScreenDetails
from python.pygame.Game_3.player import Player
from python.pygame.Game_3.points import Points

def main():
    screen = ScreenDetails.screen
    pygame.init()
    pygame.mixer.init()
    player = Player()
    points = Points()
    Clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(ScreenDetails.screen_color)
        running = player.impact_the_wall_or_itself()
        event = pygame.event.get()
        for events in event:
            if events.type == QUIT:
                running = False
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    print('you are pressing escape')
                    running = False

        player.update(event)
        points.make_points_and_continue()
        player.length = points.collision_([player.center_x, player.center_y])
        print(player.length)
        pygame.display.flip()
        Clock.tick(30)


if __name__ == "__main__":
    main()
