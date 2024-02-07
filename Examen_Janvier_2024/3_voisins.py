def voisins(connexions):  # Ne pas effacer cette ligne
    """
    @pre: `connexions` est une liste de connexions entre villes, où chaque
          connexion est representée par une paire ('Ville1', 'Ville2') de
          noms de villes. La liste ne contient pas de doublons.
    @post: retourne un dictionnaire dont les clés sont les noms de villes, et
          les valeurs sont les liste de noms de villes avec lesquelles il y
          a une connexion. Les connexions ne sont pas dirigées.
    """
    # initialiser le dictionnaire
    dict_voisins = {}
    # pour chaque ligne de la liste
    for origin, dest in connexions:
        # récupérer les voisins des villes
        voisins_origin = dict_voisins.get(origin, [])
        voisins_dest = dict_voisins.get(dest, [])
        # vérifier les doublons (inutile ici) et ajouter l'un l'autre comme voisin
        if origin not in voisins_dest:
            voisins_dest.append(origin)
        if dest not in voisins_origin:
            voisins_origin.append(dest)

        # remettre la liste dans le dictionnaire
        dict_voisins[origin] = voisins_origin
        dict_voisins[dest] = voisins_dest

    # retourner le résultat
    return dict_voisins
