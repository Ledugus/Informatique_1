import turtle
from Robot import Robot


class TurtleBot(Robot):
    def __init__(self, nom: str):
        # nom du robot
        super().__init__(nom)
        self.__t = turtle.Turtle()

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

    def __turn(self, angle, undo=False):
        self.__t.left(angle)
        if not undo:
            self.add_move_to_history("turn", angle)

    def turn_right(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(-angle)

    def turn_left(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(angle)

    def __move(self, distance, undo=False):
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            distance pos = forward
            distance neg = backward
        """
        if not undo:
            self.__t.pendown()
            self.add_move_to_history("move", distance)
        self.__t.forward(distance)
        self.__t.penup()

    def move_forward(self, distance):
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance)

    def move_backward(self, distance):
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(-distance)

    def unplay(self):
        for _ in range(len(self.history())):
            last_move = self.history().pop()
            if last_move[0] == "move":
                self.__move(-last_move[1], undo=True)
            if last_move[0] == "turn":
                self.__turn(-last_move[1], undo=True)
