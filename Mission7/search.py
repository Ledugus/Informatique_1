def readfile(filename):
    """ Crée une liste des lignes contenues dans un fichier dont le nom est ``filename``

    Args:
        filename: le nom d'un fichier de texte
    Retourne:
        une liste dans laquelle chaque ligne du fichier filename est un élément.
        Si filename n'existe pas, la fonction retourne une liste vide.
    """
    lines = []
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

    except IOError:
        print("Fichier introuvable")
    return lines

def clean_ponctuation(word):
    new_word = ""
    for char in word:
        if char.isalpha():
            new_word = new_word + char
    return new_word
def get_words(line):
    """ pour une chaÃ®ne de caractères donnÃ©e, retourne une liste des mots dans la chaîne,
        en minuscules, et sans ponctuation, dans l'ordre d'apparence dans le texte.
        Par exemple, pour la chaîne de caractères

        "Turmoil has engulfed the Galactic Republic. The taxation of trade routes
        to outlying star systems is in dispute."

        Le résultat est

        ["turmoil", "has", "engulfed", "the", "galactic", "republic", "the",
        "taxation", "of", "trade", "routes", "to", "outlying", "star", "systems",
        "is", "in", "dispute" ]

        Un caractère est considéré comme une ponctuation si ce n'est pas une
        lettre, selon la fonction string.isalpha () .

    Args:
        line: une chaîne de caractères.
    Retourne:
        une liste des mots dans la chaÃ®ne, en minuscules, et sans ponctuation.
    """
    # On sépare les mots en utilisant les espaces comme sÃ©parateurs
    # On enlÃ¨ve les ponctuations
    # On transforme en minuscules
    words = line.split()

    words = [word.lower() for word in words]
    words = [clean_ponctuation(word) for word in words if clean_ponctuation(word) != ""]
    return words


def create_index(filename):
    """ crée un index pour le fichier avec nom ``filename``. L'index se compose
        d'un dictionnaire dans lequel pour chaque mot du fichier ``filename``
        on retrouve une liste des indices des lignes du fichier qui contiennent
        ce mot.

        Par exemple, pour un fichier avec le contenu suivant:

          While the Congress of the Republic endlessly debates
          this alarming chain of events, the Supreme Chancellor has
          secretly dispatched two Jedi Knights.

        Une partie de l'index, representÃ© comme dictionnaire, est:


          {"while": [0], "the": [0,1], "congress": [0], \
           "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

    Args:
        filename: une chaÃ®ne de caractÃ¨res
    Retourne:
        un dictionnaire avec pour chaque mot du fichier (en minuscules)
        la liste des indices des lignes qui contiennent ce mot.
    """
    index = {}
    lines = readfile(filename)
    for line_index, line in enumerate(lines):
        words = get_words(line)

        for word in words:

            if word in index:
                index[word].append(line_index)
            else:
                index[word] = [line_index]
    return index


def get_lines(words, index):
    """ Détermine les lignes qui contiennent tous les mots indexes dans ``words``,
       selon l'index ``index``.

       Par exemple, pour l'index suivant:

         index = {"while": [0], "the": [0,1], "congress": [0], \
                  "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

       La fonction retourne
         get_lines(["the"]) -> [0,1]
         get_lines(["jedi"]) -> [2]
         get_lines(["the","of"],index) -> [0,1]
         get_lines(["while","the"],index) -> [0]
         get_lines(["congress","jedi"]) -> []
         get_lines(["while","the","congress"]) -> [0]

   Args:
       words: une liste de mots, en minuscules
       index: un dictionnaire contenant pour mots (en minuscules) des listes de nombres entiers
   Retourne:
       une liste des nombres des lignes contenant tous les mots indiqués
    """
    lines = []
    if words:
        lines = index.get(words[0], [])
    for word in words[1:]:
        liste_du_mot = index.get(word, [])
        lines = [value for value in liste_du_mot if value in lines]  # renvoie l'intersection entre les 2 listes
    return lines
