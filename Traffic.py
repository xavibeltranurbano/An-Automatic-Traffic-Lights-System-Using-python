import pygame
from Vehicle import Vehicle
from Traffic_Light import Traffic_Light
from Pedestrian import Pedestrian
import sys
import threading
import copy
import random


class Traffic:
    """ This class is used to simulate the real trafic of both pedestrian and vehicles of an intersection.
    In the simulation, we will observe that randomly, some infractions of both vehicles and pedestrians are done.
    Attributes
   -------------
    vecVehicles : vector of Vehicle()
         This vector stores all the vehicles of the traffic.
    copy_vecVehicles : vector of Vehicle()
         This vector is a copy of the initial vecVehicles vector. It is used to add new vehicles in the same initial position of the several vehicles of the vecVehicles vector.
    vec_Traffic_Light : vector of Traffic_Light()
         This vector stores all the vehicle Traffic_Lights of the traffic.
    vec_Traffic_Light_Pedestrian : vector of Traffic_Light()
         This vector stores all the pedestrian Traffic_Lights of the traffic.
    vec_Pedestrian : vector of Pedestrian()
         This vector stores all the pedestrians in the traffic.
    stop_lines : vector of points (x,y)
         This vector stores the position of the points at which the vehicles have to stop.
    tl_position : int
        PROBABLY WE WILL HAVE TO REMOVE THIS VARIABLE
    infraction : boolean
        This variable is used to know when the infractions are done (default False).
    coordx : int
        This variable is used to put a display message (when an infraction is done) in the "x" corresponding position (default 0).
    coordy : int
        This variable is used to put a display message (when an infraction is done) in the "y" corresponding position (default 0).
    rot_points : vector of points (x,y)
        This vector stores the position of the points at which the vehicles have to turn.
"""

    def __init__(self):
        """ The goal of this function is to create the previously mentioned attributes of this class."""
        vec = [1, 2, 3, 4]
        self.vecVehicles = [Vehicle(30, 366, "right", random.choice(vec)), Vehicle(414, 30, "down", random.choice(vec)),
                            Vehicle(830, 336, "left", random.choice(vec)), Vehicle(442, 670, "up", random.choice(vec))]
        self.copy_vecVehicles = [Vehicle(30, 366, "right", random.choice(vec)),
                                 Vehicle(414, 30, "down", random.choice(vec)),
                                 Vehicle(830, 336, "left", random.choice(vec)),
                                 Vehicle(442, 670, "up", random.choice(vec))]
        self.vec_Traffic_Light = [Traffic_Light(200, 395, 'green', 2, 0, "right"),
                                  Traffic_Light(310, 110, 'red', 3, 0, "down"),
                                  Traffic_Light(560, 225, 'red', 4, 0, "left"),
                                  Traffic_Light(480, 490, 'red', 1, 0, "up")]
        self.vec_Traffic_Light_Pedestrian = [Traffic_Light(288, 395, 'red', 3, 1, "right"),
                                             Traffic_Light(288, 247, 'red', 1, 1, "right"),
                                             Traffic_Light(325, 210, 'green', 4, 1, "right"),
                                             Traffic_Light(473, 210, 'green', 2, 1, "right"),
                                             Traffic_Light(512, 247, 'red', 1, 1, "right"),
                                             Traffic_Light(512, 395, 'red', 3, 1, "right"),
                                             Traffic_Light(472, 437, 'green', 2, 1, "right"),
                                             Traffic_Light(325, 437, 'green', 4, 1, "right")]
        self.vec_Pedestrian = [Pedestrian(388, 0, "down", 1), Pedestrian(859, 309, "left", 2),
                               Pedestrian(0, 378, "right", 3), Pedestrian(457, 703, "up", 4)]

        self.vec_Pedestrian_copy = [Pedestrian(388, 0, "down", 1), Pedestrian(859, 309, "left", 2),
                                    Pedestrian(0, 378, "right", 3), Pedestrian(457, 703, "up", 4)]
        self.stop_lines = [(250, 364), (414, 180), (590, 334), (492, 516)]
        self.tl_position = 0
        self.infraction = False
        self.iteration = 0
        self.pedestrian_iteration = 0
        self.pedestrian_infraction = False
        self.coordx = 0
        self.coordy = 0
        self.coordx2 = 0
        self.coordy2 = 0
        self.rot_points = [398, 426, 456, 428, 382, 352, 322, 348]
        self.pedestrian_corners = [(388, 309), (457, 309), (388, 378), (457, 378)]
        self.zebra_cross = [(302, 309), (388, 236), (457, 236), (535, 309), (535, 378), (457, 457), (388, 457),
                            (302, 378)]

    def display_Vehicles(self):
        """ The aim of this function is to display the different vehicles in the vector "self.vecVehicles" on the background. In order to
        rotate the vehicles in the road curve, we display the vehicles from their center point.
            Argument : None
            Returns: None
         """
        for Vehicle in self.vecVehicles:
            Vehicle_figure = pygame.image.load(Vehicle.return_image())  # Loads the vehicle image from a file
            if Vehicle.rotating_direction != '':  # Checks that the vehicle is  rotating
                Vehicle_figure = Vehicle.return_rotated_image(Vehicle.rotating,
                                                              Vehicle.rotating_direction)  # Rotates the vehicle image
            rect = Vehicle_figure.get_rect()  # Saves the position and size of the vehicle image
            self.screen.blit(Vehicle_figure, (
            Vehicle.posx - rect.width / 2, Vehicle.posy - rect.height / 2))  # Displays the vehicle image

    def add_Traffic_Lights(self):
        """ The aim of this function is to display the different traffic lights ( which is called "Traffic_Light in this project" )
        in their specific position. There are 2 types of traffic lights: vehicle traffic lights (stored in the vector "self.vec_Traffic_Light"
        and pedestrian traffic lights (stored in the vector "vec_Traffic_Light_Pedestrian").
            Argument : None
            Returns: None
         """
        # We display the vehicle traffic lights
        for Traffic_Light in self.vec_Traffic_Light:
            image = Traffic_Light.return_image()
            Tlight_figure = pygame.image.load(image)
            self.screen.blit(Tlight_figure, (Traffic_Light.posx, Traffic_Light.posy))
        # We display the pedestrian traffic lights
        for Traffic_Light in self.vec_Traffic_Light_Pedestrian:
            image = Traffic_Light.return_image()
            Tlight_figure = pygame.image.load(image)
            self.screen.blit(Tlight_figure, (Traffic_Light.posx, Traffic_Light.posy))

    def vec_same_direction(self, direction):
        """ The goal of this function is to return a vector containing all vehicles driving in the specified direction
        (specified by the variable "direction").
            Argument :
                ·direction : `str`. This variable is used to create a vector of Vehicles() which are driving in that specific direction.
            Returns: vector of `Vehicle`
         """
        Vehicle_direction = []
        for vehicle in self.vecVehicles:
            if vehicle.return_direction_copy() == direction:
                Vehicle_direction.append(vehicle)
        return Vehicle_direction

    def check_other_Vehicles(self, Vehicle, value):
        """ The goal of this function is to return True if there is no vehicle in front of the vehicle  called "Vehicle" ,
            or False otherwise.
                Argument :
                    ·Vehicle : `Vehicle`. This variable contains the vehicle which will check for others in front of it.
                    ·value: `int`. If value==0 it means that we want to check if we can add a vehicle or not.
                Returns: vector of `Vehicle`
         """
        direction = Vehicle.return_direction_copy()
        Vehicle_direction = self.vec_same_direction(direction)
        Vehiclex, Vehicley = Vehicle.return_position()
        distance = 80  # This value determine the distance we want to leave between two vehicles
        if value == 1:
            index = Vehicle_direction.index(Vehicle)
            if index == 0:  # If the vehicle is in the first position
                return False
            else:
                vex, vey = Vehicle_direction[
                    index - 1].return_position()  # We check the vehicle in front of the vehicle we are checking
                if (direction == "right" and Vehiclex + distance > vex) or (
                        direction == "down" and Vehicley + distance > vey) or (
                        direction == "left" and Vehiclex - distance < vex) or (
                        direction == "up" and Vehicley - distance < vey):
                    return True
        else:
            if len(Vehicle_direction) == 0:  # If there is no vehicle in the specified direction
                return False
            else:
                vex, vey = Vehicle_direction[
                    len(Vehicle_direction) - 1].return_position()  # We check the position of the last vehicle
                if (direction == "right" and Vehiclex + distance > vex) or (
                        direction == "down" and Vehicley + distance > vey) or (
                        direction == "left" and Vehiclex - distance < vex) or (
                        direction == "up" and Vehicley - distance < vey):
                    return True

    def Vehicle_Infractor_Changes(self, Vehicle):
        """ The goal of this function is to perform several tasks that are performed when a vehicle is an infractor.
                Argument :
                    ·Vehicle : `Vehicle`. This variable contains the vehicle which will check.
                Returns: None
        """
        self.vehicle_infractor = Vehicle
        Vehicle.change_infractor_status()  # we change the status of this variable from True to False to avoid entering this condition in the next iteration.
        Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
        self.infraction = True  # We change the status of this variable in order to display the infraction message.
        # We define the coordinates of the message we will display for the infraction done.
        if Vehicle.return_direction() == "right":
            self.coordx = 50
            self.coordy = 500
        elif Vehicle.return_direction() == "left":
            self.coordx = 550
            self.coordy = 75
        elif Vehicle.return_direction() == "down":
            self.coordx = 40
            self.coordy = 100
        elif Vehicle.return_direction() == "up":
            self.coordx = 575
            self.coordy = 500

    def check_position_vehicle(self, Vehicle):
        """ The goal of this function is to move the vehicles when they are after the stop line and check if the vehicles are in front of the zebra crossing.
                Argument :
                    ·Vehicle : `Vehicle`. This variable contains the vehicle which will check.
                Returns: None
        """
        direction = ["right", "down", "left", "up"]
        i = direction.index(Vehicle.return_direction())
        sx, sy = self.stop_lines[i]
        Vehiclex, Vehicley = Vehicle.return_position()
        if self.vec_Traffic_Light[i].isGreen():
            Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
        else:
            if (Vehicley < sy and Vehicle.return_direction() == "up") or (
                    Vehiclex < sx and Vehicle.return_direction() == "left"):  # We will enter in this conditional if the vehicle is after the stop_line.
                if (Vehicley == 286 and Vehicle.direction == "up") or (
                        Vehiclex == 352 and Vehicle.direction == "left"):  # we check if is in front of the zebra crossing
                    self.detect_pedestrians(Vehicle)
                Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
            elif (Vehicley > sy and Vehicle.return_direction() == "down") or (
                    Vehiclex > sx and Vehicle.return_direction() == "right"):  # We will enter in this conditional if the vehicle is after the stop_line.
                if (Vehicley == 406 and Vehicle.direction == "down") or (
                        Vehiclex == 484 and Vehicle.direction == "right"):  # we check if is in front of the zebra crossing
                    self.detect_pedestrians(Vehicle)
                Vehicle.change_position()  # We change the position of the vehicle depending on its direction.

    def set_turning_parameters(self, Vehicle):
        """ The goal of this function is to set the parameters (rotation point and next direction) of the vehicle that is going to rotate depending of its current direction and its turning direciton.
            Argument :
                ·Vehicle : `Vehicle`. This variable contains the vehicle that wil rotate.
            Returns:
                ·rot_point: `Int`. This variable saves the starting point of the rotation.
                ·next_dir: `Str`. This variable contains the direction the vehicle will move after turning.
        """
        if Vehicle.return_direction() == "right":
            if Vehicle.rotating_direction == "right":
                rot_point = self.rot_points[
                    0]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "down"  # Saves the direction of the vehicle after turning
            elif Vehicle.rotating_direction == "left":
                rot_point = self.rot_points[
                    1]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "up"  # Saves the direction of the vehicle after turning
        if Vehicle.return_direction() == "left":
            if Vehicle.rotating_direction == "right":
                rot_point = self.rot_points[
                    2]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "up"  # Saves the direction of the vehicle after turning
            elif Vehicle.rotating_direction == "left":
                rot_point = self.rot_points[
                    3]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "down"  # Saves the direction of the vehicle after turning
        if Vehicle.return_direction() == "up":
            if Vehicle.rotating_direction == "right":
                rot_point = self.rot_points[
                    4]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "right"  # Saves the direction of the vehicle after turning
            elif Vehicle.rotating_direction == "left":
                rot_point = self.rot_points[
                    5]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "left"  # Saves the direction of the vehicle after turning
        if Vehicle.return_direction() == "down":
            if Vehicle.rotating_direction == "right":
                rot_point = self.rot_points[
                    6]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "left"  # Saves the direction of the vehicle after turning
            elif Vehicle.rotating_direction == "left":
                rot_point = self.rot_points[
                    7]  # Saves the rotation point coordinates according to the direction of the vehicle and the direction it is going to turn to.
                next_dir = "right"  # Saves the direction of the vehicle after turning
        return rot_point, next_dir

    def move_Vehicles(self):
        """ The goal of this function is to move de different vehicles stored in the vector "self.vecVehicles".
                Argument : None
                Returns: None
        """
        for Vehicle in self.vecVehicles:
            Vehiclex, Vehicley = Vehicle.return_position()
            # Vehicle 1
            if Vehicle.direction == "right":
                sx, sy = self.stop_lines[0]
                if Vehiclex > sx - 5:  # the aim of the number 5 is to include all the different vehicles, since the images of some of them have different sizes.
                    if self.vec_Traffic_Light[0].isRed() and Vehicle.isInfractor() == True:
                        self.Vehicle_Infractor_Changes(Vehicle)
                if Vehiclex == sx:  # We will enter in this conditional if the vehicle is in the same position than the stop line.
                    Vehicle.decide_direction()
                if Vehiclex < sx and (not self.check_other_Vehicles(Vehicle,
                                                                    1)):  # We will enter in this conditional if the vehicle is before the stop line and there are no vehicles in front of it.
                    Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
                else:
                    self.check_position_vehicle(Vehicle)

            # Vehicle 2
            if Vehicle.direction == "down":
                sx, sy = self.stop_lines[1]
                if Vehicley >= sy - 5:  # the aim of the number 5 is to include all the different vehicles, since the images of some of them have different sizes.
                    if self.vec_Traffic_Light[1].isRed() and Vehicle.isInfractor() == True:
                        self.Vehicle_Infractor_Changes(Vehicle)
                if Vehicley == sy:  # We will enter in this conditional if the vehicle is in the same position than the stop line.
                    Vehicle.decide_direction()
                if Vehicley < sy and (not self.check_other_Vehicles(Vehicle,
                                                                    1)):  # We will enter in this conditional if the vehicle is before the stop line and there are no vehicles in front of it.
                    Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
                else:
                    self.check_position_vehicle(Vehicle)

            # Vehicle 3
            if Vehicle.direction == "left":
                sx, sy = self.stop_lines[2]
                if Vehiclex < sx + 5:  # the aim of the number 5 is to include all the different vehicles, since the images of some of them have different sizes.
                    if self.vec_Traffic_Light[2].isRed() and Vehicle.isInfractor() == True:
                        self.Vehicle_Infractor_Changes(Vehicle)
                if Vehiclex == sx:  # We will enter in this conditional if the vehicle is in the same position than the stop line.
                    Vehicle.decide_direction()
                if Vehiclex > sx and (not self.check_other_Vehicles(Vehicle,
                                                                    1)):  # We will enter in this conditional if the vehicle is before the stop line and there are no vehicles in front of it.
                    Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
                else:
                    self.check_position_vehicle(Vehicle)

            # Vehicle 4
            if Vehicle.direction == "up":
                sx, sy = self.stop_lines[3]
                if Vehicley < sy + 5:  # the aim of the number 5 is to include all the different vehicles, since the images of some of them have different sizes.
                    if self.vec_Traffic_Light[3].isRed() and Vehicle.isInfractor() == True:
                        self.Vehicle_Infractor_Changes(Vehicle)
                if Vehicley == sy:  # We will enter in this conditional if the vehicle is in the same position than the stop line.
                    Vehicle.decide_direction()
                if Vehicley > sy and (not self.check_other_Vehicles(Vehicle,
                                                                    1)):  # We will enter in this conditional if the vehicle is before the stop line and there are no vehicles in front of it.
                    Vehicle.change_position()  # We change the position of the vehicle depending on its direction.
                else:
                    self.check_position_vehicle(Vehicle)

            # Rotation
            if Vehicle.rotating_direction != '':  # Checks if the vehicle is going to turn
                rot_point, next_dir = self.set_turning_parameters(Vehicle)

                # If the vehicle is in the rotating point, the rotation will start.
                if (
                        Vehicle.return_direction() == "right" or Vehicle.return_direction() == "left") and Vehicle.posx == rot_point:
                    Vehicle.start_rotation()  # Changes the attribute "rotation" of the object Vehicle to 1 in order to start the iterations for the rotation.
                if (
                        Vehicle.return_direction() == "up" or Vehicle.return_direction() == "down") and Vehicle.posy == rot_point:
                    Vehicle.start_rotation()

                i = Vehicle.rotating  # Saves the value of the attribute "rotation" of the object Vehicle.

                if i < 10 and i > 0:
                    Vehicle.rotate(
                        Vehicle.rotating_direction)  # Changes the (x,y) coordinates of the vehicle according to its current and next direction while turning.
                    Vehicle.start_rotation()  # Increments the value of the attribute "rotation" of the object Vehicle.
                    i = Vehicle.rotating  # Saves the value of the attribute "rotation" of the object Vehicle.
                    if i == 10:  # Last iteration
                        Vehicle.change_direction(
                            next_dir)  # Changes the "direction" attribute of the Vehicle object to the new direction after turning.
                        Vehicle.end_rotation()  # Sets the "rotation" attribute to 0 and erases the "rotating_direciton" attribute to end the rotation.

    def change_Traffic_Light_pedestrian(self):
        """ The goal of this function is to change the colour of the pedestrian traffic lights.
            Argument : None
            Returns: None
        """
        odd = [0, 1, 4,
               5]  # This vector contain the position of the pedestrian traffic lights that all the time have the same colour.
        for i in range(len(self.vec_Traffic_Light_Pedestrian)):
            if self.tl_position % 2 == 0:  # When this condition is True it means that the pedestrian traffic lights that are in the position "0,1,4,5" of the vector "self.vec_Traffic_Light_Pedestrian" have to be red.
                if i in odd:
                    self.vec_Traffic_Light_Pedestrian[i].change_color("red")
                else:
                    self.vec_Traffic_Light_Pedestrian[i].change_color("green")
            else:
                if i in odd:
                    self.vec_Traffic_Light_Pedestrian[i].change_color("green")
                else:
                    self.vec_Traffic_Light_Pedestrian[i].change_color("red")

    def change_colour_Traffic_Light(self):
        """ The goal of this function is to change the colour of the traffic lights from yellow to red or from red to green.
            Argument : None
            Returns: None
        """
        self.vec_Traffic_Light[self.tl_position].change_color("red")  # We change the colour from yellow to red
        if self.tl_position < (len(self.vec_Traffic_Light) - 1):
            self.vec_Traffic_Light[self.tl_position + 1].change_color("green")
            self.tl_position += 1
        else:
            self.vec_Traffic_Light[0].change_color("green")
            self.tl_position = 0

        self.change_Traffic_Light_pedestrian()  # We change the pedestrian traffic lights
        t = threading.Timer(3,
                            self.change_Traffic_Light)  # We initialize the timer to change the colour from green to yellow of the traffic light we just changed, in 3 seconds.
        t.start()  # We start the timer

    def change_Traffic_Light(self):
        """ The goal of this function is to change the colour from green to yellow of the traffic lights stored in the vector "self.vec_Traffic_Light" in the position "self.tl_position".
            Argument : None
            Returns: None
        """
        self.vec_Traffic_Light[self.tl_position].change_color("yellow")
        t = threading.Timer(3,
                            self.change_colour_Traffic_Light)  # We initialize the timer to change the colour of the traffic lights we just changed, and also to change the colour of the next traffic light in the vector "self.vec_Traffic_Light", in 3 seconds.
        t.start()  # We start the timer

    def add_another_Vehicle(self):
        """ The goal of this function is to add vehicles to the intersection traffic.
            Argument : None
            Returns: None
         """
        t = threading.Timer(2, self.add_another_Vehicle)  # We initialise the timer
        for i in range(len(self.copy_vecVehicles)):
            type_vehicle = random.choice([1, 2, 3, 4])  # We choose a random vehicle
            x, y = self.copy_vecVehicles[i].return_position()  # We obtain the position of the vehicle we want to add
            Vehicle1 = Vehicle(x, y, self.copy_vecVehicles[i].return_direction(),
                               type_vehicle)  # We create the vehicle we want to add
            if not self.check_other_Vehicles(self.copy_vecVehicles[i],
                                             0):  # If there is no vehicles in the position we want to add the vehicle, this condition will be True, otherwise, will be False,
                self.vecVehicles.append(Vehicle1)
        t.start()

    def display_Traffic_Light(self):
        """ The goal of this function is to display both pedestrian and vehicles traffic lights.
            Argument : None
            Returns: None
         """
        for Traffic_Light in self.vec_Traffic_Light:
            image = Traffic_Light.return_image()  # We read the directory where the image is stored
            Vehicle_figure = pygame.image.load(image)  # We load the image
            self.screen.blit(Vehicle_figure, (Traffic_Light.posx, Traffic_Light.posy))
        for Traffic_Light in self.vec_Traffic_Light_Pedestrian:
            image = Traffic_Light.return_image()  # We read the directory where the image is stored
            Vehicle_figure = pygame.image.load(image)  # We load the image
            self.screen.blit(Vehicle_figure, (Traffic_Light.posx, Traffic_Light.posy))

    def delete_Pedestrians(self):
        """ The goal of this function is to delete the pedestrian from the pedestrian vector when they reach the edges of the screen and to generate a new one afterwards.
        The position of the new pedestrian will be chosen randomly between the positions of the initial pedestrians.
            Argument: None
            Returns: None
        """
        for Pedestrian in self.vec_Pedestrian:
            posx, posy = Pedestrian.return_position()
            if posx > 859 or posy > 703 or posx < 0 or posy < 0:  # Checks if the position of the pedestrian is in one of the edges of the screen
                self.vec_Pedestrian.remove(Pedestrian)
                Pedestrian1 = copy.copy(random.choice(
                    self.vec_Pedestrian_copy))  # Creates a new pedestrian from the original vector of pedestrian
                self.vec_Pedestrian.append(Pedestrian1)

    def check_traffic_light(self, i):
        """ The goal of this function is return the traffic light that the pedestrian has to check depending of the zebra cross it is in.
            Argument: i. Int. Represents the zebra cross.
            Returns: Traffic_Light(). Object of the class Traffic Light that represents the pedestrian traffic light that the pedestrian has to check.
        """
        if (i == 0 or i == 7 or i == 3 or i == 4):
            return self.vec_Traffic_Light_Pedestrian[5]
        elif (i == 1 or i == 2 or i == 5 or i == 6):
            return self.vec_Traffic_Light_Pedestrian[7]

    def move_pedestrians(self):
        """ The goal of this function is to control the movement of the pedestrians.
            Argument: None
            Returns: None
        """

        for pedestrian in self.vec_Pedestrian:
            x, y = pedestrian.return_position()

            # If the pedestrian is in one of the corners, it changes its direction according to the path it is in.
            for i in range(len(self.pedestrian_corners)):
                if self.pedestrian_corners[i] == (x, y):
                    pedestrian.change_direction(i, "corner")

            # If the pedestrian reaches the end of the zebra cross, it will decide its next direction randomly (left or right) to continue walking.
            if pedestrian.state == "crossing":
                if ((pedestrian.direction == "right" and x == 457) or (
                        pedestrian.direction == "left" and x == 388)) and pedestrian.already_crossed == 0:
                    pedestrian.change_direction(0, "after crossing")
                    pedestrian.crossed(1)
                elif ((pedestrian.direction == "up" and y == 309) or (
                        pedestrian.direction == "down" and y == 378)) and pedestrian.already_crossed == 0:
                    pedestrian.change_direction(0, "after crossing")
                    pedestrian.crossed(1)

            for i in range(len(self.zebra_cross)):
                if self.zebra_cross[i] == (x, y):  # Checks if the pedestrian is in front of a zebra cross
                    if pedestrian.already_crossed == 0:  # and that it has not crossed it yet
                        if pedestrian.state == "walking":
                            if pedestrian.decide_direction() == 1:  # Decides randomly whether to cross or not. If the result is to cross changes the state of the pedestrian and its direction to cross
                                pedestrian.change_state("crossing")
                                pedestrian.change_direction(i, "before crossing")
                        # Depending of the zebra cross the pedestrian is at, it checks the corresponding traffic light. If it is red it stops, otherwise it continues.
                        if pedestrian.state == "crossing":
                            if self.check_traffic_light(i).isGreen():
                                pedestrian.change_stop(0)
                            else:
                                if pedestrian.infractor == 0:
                                    pedestrian.change_stop(1)
                                else:
                                    pedestrian.change_stop(0)

                    elif pedestrian.already_crossed == 1:  # If the pedestrian is at a crossing point but it is because it has just crossed, it changes its state.
                        pedestrian.change_state("walking")
                        pedestrian.crossed(0)  # Changes the attribute "already_crossed" to 0 before continuing walking.

            pedestrian.change_position()  # Changes the coordinates of the pedestrian if it is not waiting for a green light at a zebra cross.

    def display_pedestrians(self):
        """ The aim of this function is to display the pedestrians on the vector "self.vec_Pedestrian" on the background.
        There are two different images that are displayed alternatively to simulate that the pedestrian is walking. They are changed every 10 iterations because otherwise the change is not visible.
            Argument: None
            Returns: None
        """
        for pedestrian in self.vec_Pedestrian:
            if self.iteration == 10:  # At the tenth iteration, if the pedestrian is not stopped, the image changes.
                if pedestrian.stop == 0:
                    pedestrian.change_image()
                self.iteration = 0  # Reinitializes the iteration
            else:
                self.iteration += 1
            pedestrian_figure = pygame.image.load(pedestrian.return_image(pedestrian.i))
            self.screen.blit(pedestrian_figure, (
            pedestrian.posx, pedestrian.posy))  # The corresponding image is displayed in the corresponding position.

    def detect_pedestrians(self, vehicle):
        """ The goal of this function is to detect if there is a pedestrian crossing a zebra cross after the vehicle turns in order to make it stop until the pedestrian passes.
            Argument:
                ·Vehicle : `Vehicle`. Vehicle object that is near the zebra cross after turning and needs to check that there are no pedestrians crossing before continuing-
            Returns: None
        """
        detected = 0  # This variable equals 0 if no pedestrian is detected in the zebra cross or 1 otherwhise.

        # Checks if there are pedestrians in the crossing line corresponding to the direction of the vehicle when the vehicle reaches the zebra cross
        # If any pedestrian is found, the "detected" variable turns 1.
        if self.vec_Traffic_Light_Pedestrian[5].isGreen():
            if vehicle.direction == "right":
                for pedestrian in self.vec_Pedestrian:
                    if pedestrian.state == "crossing" and pedestrian.posx == 535:
                        detected = 1
            if vehicle.direction == "left":
                for pedestrian in self.vec_Pedestrian:
                    if pedestrian.state == "crossing" and pedestrian.posx == 302:
                        detected = 1
        if self.vec_Traffic_Light_Pedestrian[7].isGreen():
            if vehicle.direction == "up":
                for pedestrian in self.vec_Pedestrian:
                    if pedestrian.state == "crossing" and pedestrian.posy == 236:
                        detected = 1
            if vehicle.direction == "down":
                for pedestrian in self.vec_Pedestrian:
                    if pedestrian.state == "crossing" and pedestrian.posy == 457:
                        detected = 1

        vehicle.save_detected(
            detected)  # Saves the value of the "detected" variable in the attribute "detected" of the object Vehicle entered as an argument of the function.

    def only_traffic_light_vehicle(self, vec):
        """ The goal of this function is to return a vector with the vehicles that are before the traffic light.
                 Argument :
                    ·vec: vector of `Vehicle`. This vector stores the different vehicles that are going to be checked.
                 Returns: vector of `Vehicles`.
        """
        vec_vehicles_only = []
        for vehicle in vec:
            posx, posy = vehicle.return_position()
            if posx <= 250 and vehicle.return_direction() == "right":  # if the position x is lower or equal than 250, it means that the vehicle is located before the traffic light.
                vec_vehicles_only.append(vehicle)
            if posy <= 180 and vehicle.return_direction() == "down":  # if the position y is lower or equal than 180, it means that the vehicle is located before the traffic light.
                vec_vehicles_only.append(vehicle)
            if posx >= 590 and vehicle.return_direction() == "left":  # if the position x is bigger or equal than 590, it means that the vehicle is located before the traffic light.
                vec_vehicles_only.append(vehicle)
            if posy >= 516 and vehicle.return_direction() == "up":  # if the position y is bigger or equal than 516, it means that the vehicle is located before the traffic light.
                vec_vehicles_only.append(vehicle)
        return vec_vehicles_only

    def find_pedestrian_infraction(self):
        """ The goal of this function is to find a pedestrian to perform an infraction.
                Argument : None
                Returns: None
        """
        for pedestrian in self.vec_Pedestrian:
            x, y = pedestrian.return_position()  # Saves the current position of the pedestrian
            for i in range(len(self.zebra_cross)):
                if self.zebra_cross[i] == (x, y) and self.check_traffic_light(
                        i).isGreen() == False:  # Checks if the pedestrian is in a zebra cross waiting to cross because the traffic light is red.
                    pedestrian.become_infractor()  # Changes the "infractor" attribute of the object of the class "Pedestrian" to 1.
                    self.pedestrian_infraction_changes(
                        pedestrian)  # Makes the necessary changes to display the infraction message.
                    #print("FOUND")
                    break

    def pedestrian_infraction_changes(self, pedestrian):
        """ The goal of this function is to make the necessary changes to display the infraction message.
                Argument :
                    · pedestrian: `Pedestrian`. Infractor pedestrian.
                Returns: None
        """
        self.pedestrian_infraction = True  # This value is used for displaying the infraction message.
        posx, posy = pedestrian.return_position()  # Saves the current position of the pedestrian to know in which zebra cross it is.

        for i in range(len(self.zebra_cross)):
            if self.zebra_cross[i] == (posx, posy):  # Finds the zebra cross where the pedestrian is.
                break

        # Sets the values of the attributes "coordx2" and "coordy2" depending on the zebra cross where the pedestrian is.
        # These variables are used to display the infraction message in the right possition, close to the infraction.
        if i == 6 or i == 7:
            self.coordx2 = 50
            self.coordy2 = 500
        elif i == 2 or i == 3:
            self.coordx2 = 550
            self.coordy2 = 75
        elif i == 0 or i == 1:
            self.coordx2 = 40
            self.coordy = 100
        elif i == 4 or i == 5:
            self.coordx2 = 575
            self.coordy2 = 500

    def find_vehicle_infraction(self):
        """ The goal of this function is to find a vehicle to perform an infraction.
                 Argument : None
                 Returns: None
        """
        position = random.choice([0, 1, 2, 3])
        direction = ["right", "down", "left", "up"]  # We choose a random direction
        vec_vehicles_all = self.vec_same_direction(direction[position])
        vec_vehicles_only = self.only_traffic_light_vehicle(vec_vehicles_all)
        if len(vec_vehicles_only) != 0:  # If there is at least one vehicle for the chosen direction, this conditional will be True. Otherwise, it will be False.
            vehicle = vec_vehicles_only[0]
            posx, posy = vehicle.return_position()
            # Those conditions work in order to display the infraction if the vehicle is close to the position of the corresponding stop line.
            if posx >= 245 and vehicle.return_direction() == "right":
                vehicle.become_infractor()  # We change the status of the attribute called infractor of this vehicle.
            elif posy >= 175 and vehicle.return_direction() == "down":
                vehicle.become_infractor()  # We change the status of the attribute called infractor of this vehicle.
            elif posx <= 585 and vehicle.return_direction() == "left":
                vehicle.become_infractor()  # We change the status of the attribute called infractor of this vehicle.
            elif posy <= 511 and vehicle.return_direction() == "up":
                vehicle.become_infractor()  # We change the status of the attribute called infractor of this vehicle.

    def remove_vehicle_infractor(self):
        """ The goal of this function is to remove the infractor.
                 Argument : None
                 Returns: None
        """
        self.iteration = 1  # We change the status of this attribute to remove the displayed message.
        if self.vehicle_infractor in self.vecVehicles:  # We check if the infractor vehicle is in the vector "self.vecVehicles"
            self.vecVehicles.remove(self.vehicle_infractor)  # We remove the infractor vehicle from the vector

        self.infraction = False  # We change the status of this variable from True to False

    def remove_pedestrian_infractor(self):
        """ The goal of this function is to remove the infractor.
                 Argument : None
                 Returns: None
        """

        self.pedestrian_iteration = 0  # Changes the value of the attribute in order to remove the infraction message from the screen.
        for pedestrian in self.vec_Pedestrian:
            if pedestrian.infractor == 1:  # Finds the infractor pedestrian
                self.vec_Pedestrian.remove(pedestrian)  # Removes the infractor pedestrian
                Pedestrian1 = copy.copy(random.choice(
                    self.vec_Pedestrian_copy))  # Creates a new pedestrian from the original vector of pedestrian
                self.vec_Pedestrian.append(Pedestrian1)  # Adds this new pedestrian to the vector "vec_Pedestrian"

        self.pedestrian_infraction = False  # We change the status of this variable from True to False

    def delete_Vehicles(self):
        """ The goal of this function is to remove the vehicles that are outside the screen.
                 Argument : None
                 Returns: None
        """
        for Vehicle in self.vecVehicles:
            posx, posy = Vehicle.return_position()
            if posx > 859 or posy > 703 or posx < 0 or posy < 0:  # We check if the vehicle is out of the screen
                self.vecVehicles.remove(Vehicle)  # We remove the vehicle from the vector

    def display_infraction_message(self, type):
        """ The goal of this function is to display the infraction message on the screen.
                 Argument :
                    · type: `str`. Type of infraction ("pedestrian" or "vehicle").
                 Returns: None
        """
        if type == "vehicle":
            infraction = pygame.image.load(
                "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/infraction/infraction_message-2.png")  # Loads the image for the infraction message from a file
            self.screen.blit(infraction, (self.coordx, self.coordy))  # Displays the infraction message on the screen
            if self.iteration == 0:
                t4 = threading.Timer(3,
                                     self.remove_vehicle_infractor)  # Timer to remove the infractor vehicle and the displayed message after 3 seconds
                t4.start()
                self.iteration += 1  # This attribute is changed in order to avoid entering to this conditional again
        elif type == "pedestrian":
            infraction = pygame.image.load(
                "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/infraction/infraction_message_pedestrian.jpeg")  # Loads the image for the infraction message from a file
            self.screen.blit(infraction, (self.coordx2, self.coordy2))  # Displays the infraction message on the screen
            if self.pedestrian_iteration == 0:
                t5 = threading.Timer(3,
                                     self.remove_pedestrian_infractor)  # Timer to remove the infractor vehicle and the displayed message after 3 seconds
                t5.start()
                self.pedestrian_iteration += 1  # This attribute is changed in order to avoid entering to this conditional again

    def main_screen(self):
        """ The goal of this function is to set the window of the program, the initial screen and the infinite loop of the simulation.
            Argument : None
            Returns: None
        """

        # The size of the window is settled
        screenWidth = 859
        screenHeight = 703
        screenSize = (screenWidth, screenHeight)

        # We initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode(
            screenSize)  # Initializes the window for display with the desired size
        background = pygame.image.load(
            '/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/background2.png')  # Loads the background image from a file source
        self.screen.blit(background, (0, 0))  # Displays the background image in the screen
        pygame.display.set_caption("SIMULATION")  # Sets a title for the window
        INFRACTION = pygame.USEREVENT + 1  # Creates a customized event to create randomly an infraction.
        PEDESTRIAN_INFRACTION = pygame.USEREVENT + 2
        pygame.time.set_timer(INFRACTION,
                              10500)  # Sets the customized event "INFRACTION" to appear on the event queue every 10.5 seconds.
        pygame.time.set_timer(PEDESTRIAN_INFRACTION, 5000)
        t1 = threading.Timer(4, self.add_another_Vehicle)  # Sets a timer to add a new vehicle every 4 seconds
        t1.start()  # Starts the timer
        t2 = threading.Timer(5,
                             self.change_Traffic_Light)  # Sets a timer to change the color of the traffic lights every 5 seconds
        t2.start()  # Starts the timer

        # Infinite loop
        while True:
            self.screen.blit(background, (0, 0))  # Displays the background image
            self.screen.blit(pygame.image.load(
                "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/logos/logoUB.png"),
                             (10, 10))
            self.screen.blit(pygame.image.load(
                "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/logos/MAIA_logo.png"),
                             (750, 10))
            for event in pygame.event.get():  # Checks the events queue
                # QUIT event
                if event.type == pygame.QUIT:
                    pygame.quit()  # Desactivates pygame library
                    sys.exit()  # Closes the window
                #  Vehicle INFRACTION event
                if event.type == INFRACTION:
                    #print("AN INFRACTION IS GOING TO BE DONE!")
                    self.find_vehicle_infraction()
                #  Pedestrian INFRACTION event
                if event.type == PEDESTRIAN_INFRACTION:
                    self.find_pedestrian_infraction()

            self.display_Traffic_Light()  # Displays the traffic light images on the background
            self.display_pedestrians()  # Displays the pedestrian images on the background
            self.move_Vehicles()  # Move the vehicles
            self.move_pedestrians()  # Move the pedestrians
            self.delete_Vehicles()  # Deletes the vehicles from the vector "self.vecVehicles" if they are on the out of the screen.
            self.delete_Pedestrians()  # Deletes the pedestrians from the vector "self.vec_Pedestrians" if they are on the out of the screen.
            self.display_Vehicles()  # Displays the vehicle images on the background
            if self.infraction or self.pedestrian_infraction:
                if self.infraction == True:  # If an infraction is detected
                    self.display_infraction_message("vehicle")
                    pygame.display.update()  # Updates the screen
                if self.pedestrian_infraction == True:  # If an infraction is detected
                    self.display_infraction_message("pedestrian")
                    pygame.display.update()  # Updates the screen

            pygame.display.update()  # Updates the screen