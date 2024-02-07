from linked_list import Node, LinkedList


class LinkedListWithCurrent(LinkedList):  # Ne pas effacer cette ligne
    def __init__(self):  # Ne pas effacer cette ligne
        """
        Initialise un nouvel object LinkedListWithCurrent en faisant appel à la
        méthode d'initialisation de la classe parente.
        @pre:  -
        @post: Une nouvelle instance vide de LinkedListWithCurrent a été initialisé.
               Elle a une taille de 0, ne contient pas de noeud,
               `head` est assigné à `None` et `current` est assigné à `None`.
        """
        # référence à la méthode __init__ de la classe mère
        super().__init__()
        # ajout de l'attribut supplémentaire current
        self.current = None

    def advance(self):  # Ne pas effacer cette ligne
        """
        Avance la référence `current` d'un pas en avant, comme expliqué ci-dessous.
        @pre:  -
        @post: Lorsque le noeud `current` est vide et que `advance()` est appelé, `current`
               est assigné au premier noeud (la tête) de la liste. Si il n'y a pas de
               premier noeud (la tête est `None`), alors le noeud `current` reste `None`.
               Si `current` fait déjà référence à un noeud existant, après avoir appelé
               cette méthode il fera référence au noeud suivant de ce noeud.
               Si `current` fait référence au dernier noeud de la liste, après avoir appelé
               cette méthode il sera à nouveau assigné à `None`.
               Aucune autre modification n'est apportée à cet objet LinkedListWithCurrent.
        """
        # si pas de pointeur établi, aller sur le premier noeud
        if self.current == None:
            self.current = self.first()
        # sinon, le pointeur est un noeud, next() peut donc être appelé
        # dans le cas du dernier noeud, son pointeur est None donc next() retourne la valeur désirée
        else:
            self.current = self.current.next()

    def insert_after_current(self, value):  # Ne pas effacer cette ligne
        """
        Insère un nouveau noeud avec une valeur donnée juste après le noeud `current`.
        @pre:  -
        @post: Un nouveau noeud avec la valeur donnée est créé.
               Ce noeud est ajouté juste après le noeud `current` et réfère au noeud
               suivant le noeud `current`.
               Si le noeud `current` est `None`, alors le nouveau noeud est ajouté
               au début de la liste.
               La longueur de la liste est mise à jour en conséquence.
               La référence au noeud `current` reste la même qu'avant.
        """
        # si le pointeur est vide, ajouter en tête de liste
        if self.current == None:
            self.add(value)
        # sinon, self.current est un Node, on peut donc appeler set_next()
        else:
            node = Node(cargo=value, next=self.current.next())
            self.current.set_next(node)
            self.length += 1
