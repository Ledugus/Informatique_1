def transforme(nom_fichier):  # Ne pas effacer cette ligne
    """
    pre: nom_fichier est le nom d'un fichier de données.
    post: retourne une liste de strings correspondant au fichier, comme indiqué dans l'énoncé.
    En particulier, en cas d'erreur de lecture du fichier, retourne une liste vide.
    """
    try:
        # lire le fichier
        f = open(nom_fichier)
        # créer la liste avec la taille prescrite
        line1 = f.readline()
        size = int(line1.strip())
        array = [""] * size
        # mettre la jour 'array' pour chaque ligne du fichier
        for line in f.readlines():
            pos, string = line.split("#")
            pos = int(pos.strip())
            string = string.strip()
            if pos >= 0:
                array[pos] = string
            else:
                raise (ValueError)

        # fermer le fichier
        f.close()

        # retourner le résultat
        return array
    except:
        return []
