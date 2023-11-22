"""
Classes pour la mission 9
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
"""


class Article:
    def __init__(self, d: str, p: float):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p

    def description(self) -> str:
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) -> float:
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix

    def taux_tva(self) -> float:
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """
        return 0.21  # TVA a 21%

    def tva(self) -> float:
        """
        @post: retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self) -> float:
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self) -> str:
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())


class Piece:
    def __init__(self, d: str, prix: float, poids: float=0.0, fragile=False, tva_reduit=False):
        self.__description = d
        self.__prix = prix
        self.__poids = poids
        self.__fragile = fragile
        self.__tva_reduit = tva_reduit

    def description(self) -> str:
        return self.__description

    def prix(self):
        return self.__prix

    def poids(self):
        return self.__poids

    def fragile(self):
        return self.__fragile

    def tva_reduit(self):
        return self.__tva_reduit
    
    def __eq__(self, other: 'Piece') -> bool:
        return self.description() == other.description() and self.prix() == other.prix()


class ArticlePiece(Article):
    def __init__(self, nombre: int, piece: Piece):
        self.nombre = nombre
        self.piece = piece
    
    def description(self) -> str:
        return f"{self.nombre} * {self.piece.description()} @ {self.piece.prix()}"
    
    def prix(self) -> float:
        return self.nombre * self.piece.prix()
    
    def taux_tva(self) -> float:
        return 0.06 if self.piece.tva_reduit() else super().taux_tva()

class ArticlePieceGros(ArticlePiece):
    def __init__(self, nombre: int, piece: Piece):
        super().__init__(nombre, piece)
    def prix(self):
        return self.piece.prix() * self.nombre

class ArticleReparation(Article):
    def __init__(self, duree: float):
        self.duree = duree
        super().__init__(self.description(), self.prix())

    def description(self) -> str:
        return f"Réparation ({self.duree} heures)"

    def prix(self) -> float:
        return 20 + 35 * self.duree


###############
### FACTURE ###
###############
"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
"""


class Facture:
    __current_number = 1

    def __init__(self, d, a_list: list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """

        self.id = Facture.__current_number
        Facture.__current_number += 1
        self.__description = d
        self.__articles = a_list
    def articles(self)-> list:
        return self.__articles
    def description(self):
        """
        @post: retourne la description de cette facture.
        """
        return self.__description

    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles:
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self, col1="Description", col2="prix HTVA", col3="TVA", col4="prix TVAC") -> str:
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return (
            f"Facture n°{self.id} : "
            + self.__description
            + "\n"
            + self.barre_str()
            + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format(
                col1, col2, col3, col4
            )
            + self.barre_str()
        )

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "=" * barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(
            art.description(), art.prix(), art.tva(), art.prix_tvac()
        )

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return (
            self.barre_str()
            + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(
                "T O T A L", prix, tva, prix + tva
            )
            + self.barre_str()
        )

    # Cette méthode doit être ajouté lors de l'étape 2.5 de la mission
    def nombre(self, pce: Piece) -> int:
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        count = 0
        for article in self.__articles:
            if type(article) == ArticlePiece and article.piece == pce:
                count += article.nombre
        return count
    # Cette méthode doit être ajouté lors de l'étape 2.6 de la mission
    def livraison_str(self) -> str:
        entete = "Livraison - " + self.entete_str(col2="poids/pce", col3="nombre", col4="poids")

        total_poids = 0.0
        total_nombre= 0.0
        lignes = ""
        is_fragile = False
        for art in self.__articles:
            poids_art = art.piece.poids() * art.nombre
            lignes += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(
            art.description(), art.piece.poids(), art.nombre, poids_art
        )
            total_poids += poids_art
            total_nombre += art.nombre
            if art.piece.fragile():
                is_fragile = True
        totaux_case_1 = f"{len(self.__articles)} articles"
        empty_str = ""
        totaux = (
            self.barre_str()
            + "| {0:40} | {1:10} | {2:10.2f} | {3:10.2f} |\n".format(
                totaux_case_1, empty_str, total_nombre, total_poids
            )
            + self.barre_str()
        )
        
        fragile = " (!) *** livraison fragile ***" if is_fragile else ""
        return entete + lignes + totaux + fragile

    def print_livraison(self):
        print(self.livraison_str())

piece_1 = Piece("Ampoule LED", 16.99, poids=0.1, fragile=True)
piece_1_non_fragile = Piece("Ampoule renforcée", 16.99, poids=0.1)
piece_2 = Piece("Ticket de cinema", 7.50, tva_reduit=True, poids=0.01)

articles_pieces = [ArticlePiece(5, piece_1),
                   ArticlePiece(2, piece_2),
                   ArticlePiece(3, piece_1_non_fragile)
                   ]

if __name__ == "__main__":
    facture = Facture("Ma belle facture", articles_pieces)
    print(facture)
    facture.print_livraison()
