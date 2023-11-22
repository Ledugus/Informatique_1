"""
Tests
"""
from mission9 import Article, ArticleReparation, ArticlePiece, Piece, Facture

piece_1 = Piece("Ampoule LED", 16.99, poids=0.1, fragile=True)
piece_1_non_fragile = Piece("Ampoule LED", 16.99, poids=0.1)
piece_2 = Piece("Ticket de cinema", 7.50, tva_reduit=True, poids=0.01)

articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49),
             ArticleReparation(1),
             ArticlePiece(5, piece_1),
             ArticlePiece(2, piece_2)
             ]
articles_pieces = [ArticlePiece(5, piece_1),
                   ArticlePiece(2, piece_2)
                   ]
articles_pieces_non_fragile = [ArticlePiece(2, piece_1_non_fragile),
                               ArticlePiece(5, piece_2)
                               ]

def test_articles(a_list) :
    for art in a_list :
        print(art)


facture_1 = Facture("PC Store - 22 novembre", articles)
new_list = articles[:]
new_list.append(ArticlePiece(3, piece_2))
facture_2 = Facture("Carrefour - 31 février", new_list)
facture_3 = Facture("Juste des ArticlePiece", articles_pieces)
facture_4 = Facture("Non fragile comme facture 3", articles_pieces_non_fragile)

def test_facture(f: Facture) :
    print(f"La facture {f.id} contient {f.nombre(piece_1)} fois la pièce {piece_1.description()}")
    print(f"La facture {f.id} contient {f.nombre(piece_2)} fois la pièce {piece_2.description()}")
    print(f)

"""
Faire exécuter les différents tests.
"""

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture_1)
    test_facture(facture_2)
    facture_3.print_livraison()
    facture_4.print_livraison()
