from linked_list import LinkedList


def reversed(self):  # Ne pas effacer cette ligne
    """
    Crée une nouvelle liste chaînée qui est une version inversée de cette liste.
    Pre :  -
    Post : une *nouvelle* liste chaînée est retournée, de type LinkedList contenant les mêmes
    valeurs que la liste originale, mais dans un ordre inversé. La liste
    originale n'est pas modifiée. Aucun nœud n'est partagé entre la liste
    originale et la nouvelle liste.
    """
    # Initialiser une nouvelle liste chaînée
    l = LinkedList()
    # current_node est un noeud de la liste de base
    current_node = self.first()
    while current_node is not None:
        # add crée un nouveau noeud donc pas d'effet de bord
        l.add(current_node.value())
        # on traverse la liste de next en next
        current_node = current_node.next()
    return l
