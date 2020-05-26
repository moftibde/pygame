import pygame
from python.pygame.Game_3.details import PointsDetails, ScreenDetails, PlayerDetails
import random
import math


class Points:
    def __init__(self):
        self.number_of_points_live_on_screen = PointsDetails.number_of_points_live_on_screen
        self.point_color = []
        self.point_width = PointsDetails.point_width
        self.points_centers = []
        self.started_app = False
        self.collision = False
        self.length = PlayerDetails.player_length
        self.real_point = PointsDetails.real_point

    def make_random_center_x_and_center_y_and_color_and_something_else(self):
        return [random.randint(self.point_width, ScreenDetails.screen_width - self.point_width),
                random.randint(self.point_width, ScreenDetails.screen_height - self.point_width),
                [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                self.point_width, +1, 5]

    def make_points_and_continue(self):
        if not self.started_app:
            self.started_app = True
            for i in range(self.number_of_points_live_on_screen):
                self.points_centers.append(
                    self.make_random_center_x_and_center_y_and_color_and_something_else())

        for a_point_in_tuple in self.points_centers:
            # print(a_point_in_tuple)
            pygame.draw.rect(ScreenDetails.screen, a_point_in_tuple[2],
                             (a_point_in_tuple[0] - a_point_in_tuple[3] / 2,
                              a_point_in_tuple[1] - a_point_in_tuple[3] / 2,
                              a_point_in_tuple[3], a_point_in_tuple[3]), 0)
            a_point_in_tuple[3] += a_point_in_tuple[4]
            if a_point_in_tuple[3] >= self.point_width + a_point_in_tuple[5] or a_point_in_tuple[
                3] <= self.point_width - a_point_in_tuple[5]:
                # print('yeah')

                a_point_in_tuple[4] *= -1

    def collision_(self, center):
        length = self.length
        for point_center in self.points_centers:
            distance = 50
            for i in range(2):
                distance += math.pow((point_center[i] - center[i]), 2)
            if math.sqrt(distance) < (PlayerDetails.player_width + PointsDetails.point_width) / 2:
                self.points_centers.remove(point_center)
                self.points_centers.append(
                    self.make_random_center_x_and_center_y_and_color_and_something_else())
                length += self.real_point
        self.length =length
        return length
