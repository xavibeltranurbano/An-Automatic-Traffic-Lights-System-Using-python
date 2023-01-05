class Traffic_Light:
    """
    A class used to represent an Animal
    ...
    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)
    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    def __init__(self, posx, posy, color,rotation,type,direction):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.rotation = rotation
        self.type=type
        self.direction=direction

    def return_image(self):
        if self.type==0:
            if self.color=="green":
                if self.rotation==1:
                     return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/green_light1.png"
                if self.rotation == 2:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/green_light2.png"
                if self.rotation == 3:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/green_light3.png"
                if self.rotation == 4:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/green_light4.png"

            elif self.color == "red":
                if self.rotation == 1:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/red_light1.png"
                if self.rotation == 2:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/red_light2.png"
                if self.rotation == 3:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/red_light3.png"
                if self.rotation == 4:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/red_light4.png"

            elif self.color == "yellow":
                if self.rotation == 1:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/yellow_light1.png"
                if self.rotation == 2:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/yellow_light2.png"
                if self.rotation == 3:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/yellow_light3.png"
                if self.rotation == 4:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/yellow_light4.png"
        else:
            if self.color == "green":
                if self.rotation == 1:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_green1.png"
                if self.rotation == 2:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_green2.png"
                if self.rotation == 3:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_green3.png"
                if self.rotation == 4:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_green4.png"

            elif self.color == "red":
                if self.rotation == 1:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_red1.png"
                if self.rotation == 2:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_red2.png"
                if self.rotation == 3:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_red3.png"
                if self.rotation == 4:
                    return "/Users/xavibeltranurbano/Desktop/MASTER/1rst YEAR/SOFTWARE ENGINEER/TRAFFIC PROJECT/images/semaforos_images/pedestrian_red4.png"

    def return_poscition(self):
        return self.posx,self.posy

    def return_direction(self):
        return self.direction

    def change_color(self,color):
        self.color=color

    def return_color(self):
        return self.color

    def isGreen(self):
        if self.color == "green":
            return True
        else:
            return False

    def isRed(self):
        if self.color == "red":
            return True
        else:
            return False

    def isYellow(self):
        if self.color == "yellow":
            return True
        else:
            return False

