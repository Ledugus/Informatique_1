from math import pi

class Robot:
    def __init__(self,nom,x=0,y=0) :
        # nom du robot
        self.__nom = nom
        # position du robot
        self.__history = []          
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve dans le coin supérieur gauche    
    
    def __str__(self) -> str:
        return self.nom()
    def nom(self):
        return self.__nom

    def add_move_to_history(self, type: str, value: float):
        self.history().append((type, value))

    def history(self):
        return self.__history
    
    def unplay(self):
        pass
    


