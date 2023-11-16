"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

from mission9 import Article, Facture

"""
Test initial pour la classe Article.
@author Kim Mens
@version 4 novembre 2021
"""
articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49)
             ]

def test_articles(a_list) :
    for art in a_list :
        print(art)

"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles)

def test_facture(f) :
    print(f)

"""
Faire exécuter les différents tests.
"""

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)
