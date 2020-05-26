import pygame
import random


class ScreenDetails:
    screen_color = (100, 100, 100)
    screen_width = 720
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))


class PlayerDetails:
    player_width = 30
    player_color = (100, 0, 255)
    player_length = 0
    player_speed = 3


class PointsDetails:
    number_of_points_live_on_screen = 4
    point_width = 30
    real_point = 5