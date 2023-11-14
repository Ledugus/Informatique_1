class Duree:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0):
        self.h = h
        self.m = m
        self.s = s

    def to_secondes(self: 'Duree') -> int:
        return 3600 * self.h + 60 * self.m + self.s

    def to_h_m_s(self, secondes: int):
        h = secondes // 3600
        secondes = secondes % 3600
        m = secondes // 60
        s = secondes % 60

        return h, m, s

    def delta(self, d: 'Duree') -> int:
        return self.to_secondes() - d.to_secondes()

    def apres(self, d: 'Duree') -> bool:
        return True if self.to_secondes() > d.to_secondes() else False

    def ajouter(self, d: 'Duree'):
        nouvelle_duree_sec = self.to_secondes() + d.to_secondes()
        self.h, self.m, self.s = self.to_h_m_s(nouvelle_duree_sec)

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)


class Chanson():
    # A COMPLETER PAR LES ETUDIANTS
    def __init__(self, t: str, a: str, d: Duree) -> None:
        self.duree = d
        self.auteur = a
        self.titre = t

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return f"{self.titre} - {self.auteur} - {self.duree}"


class Album:
    def __init__(self, id: int, ) -> None:
        self.id = id
        self.chansons = []
        self.duree = Duree()

    def add(self, chanson: Chanson) -> bool:
        nouvelle_duree = self.duree.to_secondes() + chanson.duree.to_secondes()
        if len(self.chansons) == 99 or nouvelle_duree > 75 * 60:
            return False
        self.chansons.append(chanson)
        self.duree.ajouter(chanson.duree)
        return True

    def __str__(self) -> str:
        list_of_string = []
        title = f"Album {self.id} ({len(self.chansons)} chansons, {self.duree})"
        for index, chanson in enumerate(self.chansons):
            list_of_string.append(f"\n{index + 1:02}: {chanson}")
        return title + "".join(list_of_string)


if __name__ == "__main__":
    file = open("music-db.txt", "r")

    current_id = 1
    current_album = Album(current_id)
    album_list = [current_album]

    for line in file:
        titre, auteur, m, s = line.strip().split()
        if current_album.add(Chanson(titre, auteur, Duree(m=int(m), s=int(s)))):
            continue
        else:
            current_id += 1
            current_album = Album(current_id)
            current_album.add(
                Chanson(titre, auteur, Duree(m=int(m), s=int(s))))
            album_list.append(current_album)
    for album in album_list:
        print(album)
        print()
    file.close()
