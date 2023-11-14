##############################
# Tests pour la classe Duree #
##############################
# Kim Mens, 30-10-2021, à compléter par les étudiants

# Pour le moment, pour tester votre programme orienté objet
# vous allez encore utiliser les instructions "assert" comme
# dans les missions 5 à 7. 
# (Dans une mission futur nous introduirons le nouveau mécanisme
#  des tests unitaires qui est encore mieux approprié pour tester
#  du code orienté objet.)

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree(0,0,0)
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)

# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS
    
# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    # A COMPLETER PAR LES ETUDIANTS
    pass
    
# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    # A COMPLETER PAR LES ETUDIANTS
    
# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    # A COMPLETER PAR LES ETUDIANTS
    pass

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    # A COMPLETER PAR LES ETUDIANTS
    pass

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)

##############################
# Tests pour la classe Album #
##############################

# CREATION D'UN OBJET DE LA CLASSE Album A TESTER
# à fournir par les étudiants

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Album
# à fournir par les étudiants

# FONCTION POUR TESTER LA METHODE add DE LA CLASSE Album
# à fournir par les étudiants

# APPEL DES DIFFERENTES FONCTIONS TEST
# à fournir par les étudiants

#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# à fournir par les étudiants