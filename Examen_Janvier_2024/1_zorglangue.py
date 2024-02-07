def inverse_mots(texte):  # Ne pas effacer cette ligne
    """
    Inverse chaque mot dans une phrase donnée tout en maintenant l'ordre des mots.
    Pré : `texte` est une chaîne de caractères (possiblement vide) contenant uniquement
          des lettres et des espaces.  Chaque séquence de lettres constitue un mot.
    Post : Retourne une chaîne de caractères contenant les mots de `texte` inversés.
           L'ordre des mots et les positions des espaces sont les mêmes
           que dans `texte`, et aucun caractère n'est ajouté ni supprimé.
    """
    # initialisation des variables
    x = 0
    new_word = ""
    new_text = ""
    # tant qu'on est pas au bout du texte
    while x < len(texte):
        # si c'est un espace
        if texte[x] == " ":
            # insérer le mot établi et le supprimer
            new_text += new_word
            new_word = ""
            # ajouter l'espace
            new_text += " "
        # sinon c'est un caractère d'un mot, qui se place au ***début*** de new_word (inversion des lettres)
        else:
            new_word = texte[x] + new_word
        # incrémenter l'index
        x += 1
    # ajouter l'éventuel dernier mot (si le texte se finit par une lettre)
    new_text += new_word
    return new_text
