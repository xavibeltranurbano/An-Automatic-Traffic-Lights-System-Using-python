import random


class Pedestrian:
    """ This class is used to simulate the pedestrian movement in an intersection with zebra crosses that have traffic lights.
    Attributes
   -------------
    posx : `int`
        This attribute to describe the current position of x coordinate of the pedestrian.
    posy : `int`
        This attribute to describe the current position of y coordinate of the pedestrian.
    vel : `int`
        This attribute is to define the velocity of the pedestrian (default 1 pixel per iteration).
    direction : `str`
        This attribute is used to describe the direction of the pedestrian movement (up, down, right or left).
    i : `int`
        There are two images for the pedestrian, and they are displayed alternatively to simulate the walking. This attibute allows changing the image displayed on screen.
    state : `str`
        This variable is used to define the state of the pedestrian. There are two states: "crossing" (when it is crossing a zebra cross or waiting for it) or waking (the rest of the cases).
    stop: `boolean`
        This attribute is used to stop the movement of the pedestrian. If "stop" is 0, the pedestrian is walking, otherwise it is waiting to cross a zebra cross when the traffic light is red.
    already_crossed : `boolean`
        This attribute is to check  if the pedestrian has already crossed the zebra cross to avoid it passing again.
    """

    def __init__(self, posx, posy, direction, section):
        """ The goal of this function is to define the previously mentioned attributes of this class. """
        self.posx = posx
        self.posy = posy
        self.vel = 1
        self.direction = direction
        self.section = section
        self.i = 0
        self.state = "walking"
        self.stop = 0
        self.already_crossed = 0
        self.infractor = 0

    def return_image(self, value):
        """ The aim of this function is to return the image to display for the pedestrian, depending on its direction of movement and de value of the attribute "self.i" to simulate the walking.
            Argument :
                · value: `int. This variable is used to display the right image to simulate the walking. It can be 0 or 1.
            Returns: None
        """
        if self.direction == "up":
            if value == 1:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_up.png"
            else:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_up2.png"
        if self.direction == "right":
            if value == 1:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_right.png"
            else:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_right2.png"
        if self.direction == "down":
            if value == 1:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_down.png"
            else:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_down2.png"
        if self.direction == "left":
            if value == 1:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_left.png"
            else:
                return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/pedestrian_images/pedestrian_left2.png"

    def return_position(self):
        """ The aim of this function is to return the position (in x and y) of the pedestrian.
        Argument : None
        Returns:
            · self.posx: `int`. Attribute that describes the position of the pedestrian in the x axis.
            · self.posy: `int`. Attribute that describes the position of the pedestrian in the y axis.
        """
        return self.posx, self.posy

    def change_position(self):
        """ The aim of this function is to change the position of the pedestrian in x or y depending on the direction of the movement.
            The position will be changed only if the pedestrian is not stopped in a zebra cross.
            Argument : None
            Returns: None
        """
        if self.stop == 0:  # Checks that the pedestrian is not stopped in a zebra cross
            if self.direction == "left":
                self.posx -= self.vel
            if self.direction == "right":
                self.posx += self.vel
            if self.direction == "up":
                self.posy -= self.vel
            if self.direction == "down":
                self.posy += self.vel

    def change_image(self):
        """ The aim of this function is to change the value of the attribute "self.i" in order to change the image of the pedestrian to simulate the walking.
        Argument : None
        Returns: None
        """
        if self.i == 1:
            self.i = 0
        else:
            self.i = 1

    def return_direction(self):
        """ The aim of this function is to return the direction of the movement of the pedestrian.
        Argument : None
        Returns:
            · self.direction: `str`. Attribute that describes the direction of the movement of the pedestrian.
        """
        return self.direction

    def change_direction(self, i, type):
        """ The aim of this function is to change the direction of the pedestrian at specific situations: in corners, before crossing and after crossing.
                Argument :
                    · i: `int`. This variable represents the points where the pedestrian needs to decide the direction for its next movement.

                Returns: None
        """
        if type == "corner":
            # In this case, i is the index of the vector "pedestrian_corners" of the class "Traffic", and it represents the corner where the perdestrian is.
            if i == 0:
                if self.direction == "right":
                    self.direction = "up"
                if self.direction == "down":
                    self.direction = "left"
            elif i == 1:
                if self.direction == "left":
                    self.direction = "up"
                if self.direction == "down":
                    self.direction = "right"
            elif i == 2:
                if self.direction == "right":
                    self.direction = "down"
                if self.direction == "up":
                    self.direction = "left"
            elif i == 3:
                if self.direction == "left":
                    self.direction = "down"
                if self.direction == "up":
                    self.direction = "right"
        elif type == "before crossing":
            # In this case, i is the index of the vector "zebra_cross" of the class "Traffic", and it represents the initial point of the zebra cross.
            if i == 0 or i == 3:
                self.direction = "down"
            elif i == 1 or i == 6:
                self.direction = "right"
            elif i == 2 or i == 5:
                self.direction = "left"
            elif i == 4 or i == 7:
                self.direction = "up"
        elif type == "after crossing":
            # In this case, after crossing, the direction is chosen randomly.
            if self.direction == "up" or self.direction == "down":
                self.direction = random.choice(["right", "left"])
            elif self.direction == "right" or self.direction == "left":
                self.direction = random.choice(["up", "down"])

    def decide_direction(self):
        """ The aim of this function is to decide randomly whether to cross or not. If the result is 1, the pedestrian will cross, otherwise he will not.
            Argument : None
            Returns:
                · cross: `boolean`. Variable that represents the decision of crossing or not.
        """
        cross = random.choice([0, 1, 1,
                               1])  # Chooses randomly between 0 or 1. There are more chances for the result to be 1 because it is more interesting for the simulation.
        return cross

    def change_state(self, state):
        """ The aim of this function is to change the state of the pedestrian.
            Argument :
                · state: `str`. This variable repdesents the new state of the pedestrian. It can be "cross" if the pedestrian is going to cross or "walking" if the pedestrian has just crossed and will continue walking.
            Returns: None
        """
        self.state = state

    def crossed(self, value):
        """ The aim of this function is to change the value of the attribute "already_crossed" to avoid the pedestrian crossing again right after finishing crossing.
            Argument :
                · value: `boolean`. If it is 1, means that the pedestrian has just crossed.
            Returns: None
        """
        self.already_crossed = value

    def change_stop(self, value):
        """ The aim of this function is to change the value of the attribute "stop".
            Argument :
                .value: `boolean`. It can be 1 if the pedestrian has to stop or to 0 if the pedestrian was waiting to cross and is going to start walking.
            Returns: None
        """
        self.stop = value

    def return_stop(self):
        """ The aim of this function is to return the value of the attribute "stop".
            Argument : None
            Returns: None
        """
        return self.stop

    def become_infractor(self):
        """ The aim of this function is to change the value of the attribute "infractor" to 1. This way, the pedestrian will commit an infraction, he will try to cross when the traffic light is red.
            Argument : None
            Returns: None
        """
        self.infractor = 1
