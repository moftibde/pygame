import pygame
import math
from python.pygame.Game_3.details import PlayerDetails, ScreenDetails
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]


class Player:
    def __init__(self):
        self.keypress = pygame.key.get_pressed()
        self.length = 0  # PlayerDetails.player_length
        self.speed = PlayerDetails.player_speed
        self.width = PlayerDetails.player_width
        self.color = PlayerDetails.player_color
        self.center_x = ScreenDetails.screen_width / 2
        self.center_y = ScreenDetails.screen_height / 2
        self.bending_points = [(360.0, 240.0)]
        self.bending_distance = 0
        self.moving = [False, False, False, False]
        self.first_move = False
        self.impact = False
        self.draw()

    def update(self, event):
        bending_points = self.bending_points
        moving = self.moving
        if self.first_move:
            self.append_to_bending_points()
        self.setting(event, moving)
        self.running(moving)
        self.advanced_drawing(bending_points)
        self.calculate_all_distance_in_input_lists_points_and_set_new_length_to_self(
            bending_points)
        # print(self.bending_points)

    def running(self, moving):
        for i in range(len(moving)):
            if moving[i]:
                self.set_direction(i)

    def append_to_bending_points(self):
        self.bending_points.append((self.center_x, self.center_y))

    def setting(self, event, moving):
        for events in event:
            if events.type == KEYDOWN:

                if events.key == K_UP:
                    self.first_move = True
                    # self.bending_points.append((self.center_x, self.center_y))
                    for i in range(len(moving)):
                        if i == 0:
                            moving[i] = True
                        else:
                            moving[i] = False

                elif events.key == K_DOWN:
                    self.first_move = True
                    # self.bending_points.append((self.center_x, self.center_y))
                    for i in range(len(moving)):
                        if i == 1:
                            moving[i] = True
                        else:
                            moving[i] = False

                elif events.key == K_LEFT:
                    self.first_move = True
                    # self.bending_points.append((self.center_x, self.center_y))
                    for i in range(len(moving)):
                        if i == 2:
                            moving[i] = True
                        else:
                            moving[i] = False

                elif events.key == K_RIGHT:
                    self.first_move = True
                    # self.bending_points.append((self.center_x, self.center_y))
                    for i in range(len(moving)):
                        if i == 3:
                            moving[i] = True
                        else:
                            moving[i] = False

        self.moving = moving

    def set_direction(self, i):
        if i == 0:
            self.center_y -= self.speed
        if i == 1:
            self.center_y += self.speed
        if i == 2:
            self.center_x -= self.speed
        if i == 3:
            self.center_x += self.speed

    def collision(self):
        pass

    def draw(self):
        pygame.draw.rect(ScreenDetails.screen, self.color, (self.center_x - self.width / 2,
                                                            self.center_y - self.width / 2,
                                                            self.width, self.width), 0)

    def distance_between_two_points(self, point_one, point_two):
        distance = 0
        for i in range(len(point_one)):
            distance += math.pow((point_one[i] - point_two[i]), 2)
        return math.sqrt(distance)

    def calculate_all_distance_in_input_lists_points_and_set_new_length_to_self(self,
                                                                                bending_points):
        bending_distance = bending_points
        total_distance = 0
        for i in range(len(bending_distance)):
            if i == len(bending_distance) - 1:
                break
            total_distance += self.distance_between_two_points(bending_distance[i],
                                                               bending_distance[i + 1])
        self.bending_distance = total_distance
        length = self.length
        if total_distance > length:
            del bending_distance[0]
            self.bending_points = self.bending_points
        return total_distance

    def advanced_drawing(self, bending_points):
        # print(bending_points)
        for i in range(len(bending_points)):
            pygame.draw.rect(ScreenDetails.screen, self.color,
                             (bending_points[i][0] - self.width / 2,
                              bending_points[i][1] - self.width / 2,
                              self.width, self.width), 0)
            if i == len(bending_points) - 1:
                break

    def impact_the_wall_or_itself(self):
        # for i in range(len(self.bending_points)):
        #     if i == len(self.bending_points) - 1:
        #         break
        #     if self.bending_points[i] == [self.center_x, self.center_x]:
        #         print('yeah')
        #         return False

        if (self.center_x - self.width / 2) < 0:

            return False
        elif self.center_x + self.width > ScreenDetails.screen_width:
            return False
        elif self.center_y - self.width / 2 < 0:
            return False
        elif self.center_y + self.width / 2 > ScreenDetails.screen_height:
            return False
        else:
            return True