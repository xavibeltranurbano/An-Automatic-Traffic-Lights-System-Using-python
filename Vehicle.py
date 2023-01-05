import pygame
import random


class Vehicle:

    def __init__(self, posx, posy, direction, type):
        self.posx = posx
        self.posy = posy
        self.vel = 2
        self.direction = direction
        self.type = type

        # NEW
        self.rotating = 0
        self.rotating_direction = ''
        self.infractor = 0
        self.detected = 0
        self.direction_copy = direction

    def return_image(self):
        if self.type == 0:
            if self.direction == "left":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike_left.png"
            if self.direction == "right":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike_right.png"
            if self.direction == "up":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike_up.png"
            if self.direction == "down":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike_down.png"
        elif self.type == 1:
            if self.direction == "left":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car_left.png"
            if self.direction == "right":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car_right.png"
            if self.direction == "up":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car_up.png"
            if self.direction == "down":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car_down.png"
        elif self.type == 2:
            if self.direction == "left":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car2_left.png"
            if self.direction == "right":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car2_right.png"
            if self.direction == "up":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car2_up.png"
            if self.direction == "down":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car2_down.png"

        elif self.type == 3:
            if self.direction == "left":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car3_left.png"
            if self.direction == "right":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car3_right.png"
            if self.direction == "up":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car3_up.png"
            if self.direction == "down":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/car3_down.png"

        elif self.type == 4:
            if self.direction == "left":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike2_left.png"
            if self.direction == "right":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike2_right.png"
            if self.direction == "up":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike2_up.png"
            if self.direction == "down":
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/vehicle_images/bike2_down.png"

    def return_position(self):
        return self.posx, self.posy

    def change_position(self):
        if self.detected == 0:
            if self.direction == "left":
                self.posx -= self.vel
            if self.direction == "right":
                self.posx += self.vel
            if self.direction == "up":
                self.posy -= self.vel
            if self.direction == "down":
                self.posy += self.vel

    def return_direction(self):
        return self.direction
    def return_direction_copy(self):
        return self.direction_copy

    def change_direction(self, new_direction):
        self.direction = new_direction

    def define_rotation(self, direction):
        self.rotating_direction = direction

    def start_rotation(self):
        if self.rotating == 0:
            self.rotating = 1
        else:
            self.rotating += 1

    def return_rotated_image(self, i, dir_rotation):
        original_image = pygame.image.load(self.return_image())
        if dir_rotation == "right":
            rotated_image = pygame.transform.rotate(original_image, -9 * i)
        if dir_rotation == "left":
            rotated_image = pygame.transform.rotate(original_image, 9 * i)
        return rotated_image

    def rotate(self, dir_rotation):
        if self.return_direction == "right":
            self.posx += 1
            if dir_rotation == "right":
                self.posy += 3
            if dir_rotation == "left":
                self.posy -= 3
        elif self.return_direction == "left":
            self.posx -= 1
            if dir_rotation == "right":
                self.posy -= 3
            if dir_rotation == "left":
                self.posy += 3
        elif self.return_direction == "up":
            self.posy -= 1
            if dir_rotation == "right":
                self.posx += 3
            if dir_rotation == "left":
                self.posx -= 3
        elif self.return_direction == "down":
            self.posy += 1
            if dir_rotation == "right":
                self.posx -= 3
            if dir_rotation == "left":
                self.posx += 3

    def end_rotation(self):
        self.rotating = 0
        self.rotating_direction = ''

    def decide_direction(self):
        direction = random.choice(["straight", "right", "left"])
        if direction != "straight":
            self.define_rotation(direction)

    def become_infractor(self):
        self.infractor = 1

    def save_detected(self, value):
        self.detected = value

    def isInfractor(self):
        if self.infractor == 1:
            return True
        else:
            return False

    def change_infractor_status(self):
        self.infractor=0