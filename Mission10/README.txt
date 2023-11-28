Augustin Wezel, 29/11/2023

Pour cette mission, 3 classes sont définies : 

 - Robot (mère) : un robot avec un nom, un historique et une méthode unplay().

 - TurtleBot (fille) : on représente le robot par un turtle.Turtle(). Sont définies : 
    move_backward(), move_forward(), turn_left(), turn_right(), position(), angle(), ainsi que des méthodes privées intermédiaires

 - XYRobot (fille) : on répresente le robot par une position (x, y) et un angle (sa direction). Sont définies : 
    move_backward(), move_forward(), turn_left(), turn_right(), position(), angle(), ainsi que des méthodes privées intermédiaires

2 classes de tests permettent de tester les classes filles : TestTurtleBot et TestXYBot. Elles sont exactement identiques (à un sens de rotation près), sauf pour l'initialisation du robot
Cela permet de s'assurer que les 2 sous-classes se comportent de la même manière, en polymorphisme quasi-total