# un module pour dessiner des figures simples sur un plan XY
from graphics import GraphWin, Line, Point
from Robot import Robot
# nous avons aussi besoin des fonctions cos et sin ainsi que
# la valeur pi pour notre calcul de la position d'un point
from math import pi, cos, sin, radians


class XYRobot(Robot):

    def __init__(self, nom, x=0, y=0):
        super().__init__(nom)
        self.__x = x
        self.__y = y
        self.__angle = 0
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve dans le coin supérieur gauche
        self.__win = GraphWin()

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return super().__str__() + "@(" + str(round(self.__x)) + "," + \
            str(round(self.__y)) + ") angle: "+str(self.angle())

    def angle(self):
        "retourne l'angle en degres représentant la direction du robot"
        return self.__angle

    def position(self):
        return (self.__x, self.__y)

    def angle_rad(self):
        return radians(self.angle())

    def __set_x(self, x):
        self.__x = x

    def __set_y(self, y):
        self.__y = y

    def __set_angle(self, angle):
        self.__angle = angle

    def __draw_from(self, old_x, old_y):
        """
        méthode auxiliaire pour tracer une ligne de l'ancienne position
        (old_x,old_y) du robot à sa position (x,y) actuelle
        """
        line = Line(Point(old_x, old_y), Point(self.__x, self.__y))
        line.draw(self.__win)

    def move_forward(self, distance):
        self.__move(distance)

    def move_backward(self, distance):
        self.__move(-distance)

    def __move(self, distance, undo=False):
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si distance > 0  fait avancer le robot de distance pixels
            si distance < 0  fait reculer le robot de distance pixels
        """
        old_x = self.__x
        old_y = self.__y
        orientation_x = cos(self.angle_rad())
        orientation_y = sin(self.angle_rad())
        self.__set_x(old_x + orientation_x * distance)
        self.__set_y(old_y + orientation_y * distance)
        
        self.__draw_from(old_x, old_y)
        if not undo:
            self.add_move_to_history("move", distance)

    def turn_right(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(angle)
        

    def turn_left(self, angle=90):
        """ fait tourner le robot de 90 degrés vers la gauche
            (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-angle)
        

    def __turn(self, angle, undo=False):
        """ méthode auxiliaire pour les méthodes turn_right() et turn_left()
            si direction = 1 change l'angle du robot de 90 degrés vers la droite
                             (dans le sens des aiguilles d'une montre)
            si direction = -1 change l'angle du robot de 90 degrés vers la gauche
                             (dans le sens contraire des aiguilles d'une montre)
        """
        if not undo:
            self.add_move_to_history("turn", angle)
        self.__set_angle((self.angle() + angle) % 360)

    def unplay(self):
        for _ in range(len(self.history())):
            last_move = self.history().pop()
            if last_move[0] == "move":
                self.__move(-last_move[1], undo=True)
            if last_move[0] == "turn":
                self.__turn(-last_move[1], undo=True)

# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':

    # create robot called R2-D2 at position (100,100) and facing East,
    # to be more or less in the center of the window
    r2d2 = XYRobot("R2-D2", 100, 100)

    print(r2d2)
    # R2-D2@(100, 100) angle: 0.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150, 100) angle: 270.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.move_forward(50)
    print(r2d2)
    # R2-D2@(100, 100) angle: 90.0
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
