import turtle
from math import pi, radians, degrees
from Robot import Robot


class TurtleBot(Robot):
    def __init__(self, nom: str, x=0, y=0):
        # nom du robot
        super().__init__(nom)
        # position du robot
        self.__t = turtle.Turtle()
        self.__t.setpos(x, y)
        # angle en degres radius représentant la direction du robot
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve au milieu de la fenêtre

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return super().__str__()

    def angle(self):
        "retourne l'angle en degres représentant la direction du robot"
        return self.__t.heading()

    def position(self):
        return self.__t.pos()

    def turn_right(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__t.right(-angle)
        self.add_move_to_history("turn", -angle)

    def turn_left(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__t.left(angle)
        self.add_move_to_history("turn", angle)

    def __move(self, distance):
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            distance pos = forward
            distance neg = backward
        """
        self.__t.pendown()
        self.__t.forward(distance)
        self.__t.penup()
        self.add_move_to_history("forward", distance)

    def move_forward(self, distance):
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance)

    def move_backward(self, distance):
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(-distance)
