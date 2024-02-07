def carre_magique(m):  # Ne pas effacer cette ligne
    """
    Pre: `m` est un tableau carré de taille non-nulle contenant des nombres entiers.
    Post: vérifie que `m` est un carré magique.  Si oui, retourne la
    constante magique du carré, si non, retourne None.
    """
    # si la constante existe, elle est égale à la somme de la première ligne
    const = sum(m[0])
    # pour chaque index de ligne et de colonne
    for x in range(len(m)):
        # vérifier la somme de la ligne
        if sum(m[x]) != const:
            return None
        # vérifier la somme de la colonne
        if sum([m[i][x] for i in range(len(m))]) != const:
            return None
    # vérifier la diagonale NO-SE
    if sum([m[i][i] for i in range(len(m))]) != const:
        return None
    # vérifier la diagonale SO-NE
    if sum([m[i][len(m) - i - 1] for i in range(len(m))]) != const:
        return None
    # si toutes le conditions sont passées, la constante est vraie, on la retourne
    return const
