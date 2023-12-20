class SudokuPuzzle:
    def __init__(self, dimension):
        """
        Crée un SudokuPuzzle de dimension `dimension` avec tous les éléments initialisés à 0.
        """
        self.dimension = dimension
        self.carres = [[SudokuCarre(x, y, dimension)
                        for x in range(dimension)]
                       for y in range(dimension)]

    def get_carre(self, x, y):
        """
        Retourne le SudokuCarre qui se trouve à la position (x, y) dans ce Sudoku.
        """
        return self.carres[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le Sudoku.
        """
        s = ""
        for y in range(len(self.carres)):
            for x in range(len(self.carres[y])):
                s += str(self.get_carre(x, y))
            s += "\n"
        return s

    ##############################
    ## QUESTION 1 : GETTERS     ##
    ##############################
    def get_carre_valeurs(self, x, y):
        carre = self.get_carre(x, y)
        liste = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                liste.append(carre.get_val(j, i))
        return liste

    def get_ligne(self, ligne):
        liste = []
        y_carres = ligne // self.dimension
        y_ligne = ligne % self.dimension
        for x in range(self.dimension):
            carre = self.get_carre(x, y_carres)
            for x in range(self.dimension):
                liste.append(carre.get_val(x, y_ligne))
        return liste

    def get_colonne(self, colonne):
        liste = []
        x_carres = colonne // self.dimension
        x_col = colonne % self.dimension
        for y in range(self.dimension):
            carre = self.get_carre(x_carres, y)
            for y in range(self.dimension):
                liste.append(carre.get_val(x_col, y))
        return liste

    ################################
    ### QUESTION 2 : CORRECT     ###
    ################################
    def est_correct(self):
        bonne_liste = list(range(1, self.dimension*2+1))
        for x in range(self.dimension*2):
            if sorted(self.get_ligne(x)) != bonne_liste:
                return False
            if sorted(self.get_colonne(x)) != bonne_liste:
                return False
            if sorted(self.get_carre_valeurs(x % self.dimension, x // self.dimension)) != bonne_liste:
                return False
        return True


class SudokuCarre:

    def __init__(self, x, y, dimension):
        """
        Crée un SudokuCarre de taille `dimension` x `dimension`, avec toutes ses valeurs initialisées à 0.
        """
        self.xcoord_carre = x
        self.ycoord_carre = y
        self.cells = [[0 for x in range(dimension)]
                      for y in range(dimension)]

    def set_val(self, x, y, val):
        """
        Assigne une valeur `val` à la cellule se trouvant à la position (x, y) de ce carré.
        """
        self.cells[y][x] = val

    def get_val(self, x, y):
        """
        Retourne la valeur qui se trouve à la position (x, y) de ce carré.
        """
        return self.cells[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le contenu de ce carré.
        """
        s = "carré (" + str(self.xcoord_carre) + "," + \
            str(self.ycoord_carre) + ") : "
        s += str(self.cells)
        s += " "
        return s
