Augustin Wezel, 05/12/2023

Ce programme consiste en 5 classes qui représentent ensemble un classement d'une course

 - Temps : une quantité de temps
    - Addition, comparaison, conversion secondes <-> temps conventionnel (h, m, s)
 - Coureur : un coureur 
    - Nom, âge
    - Comparaison
 - Resultat : une entrée dans le tableau de classement
    - coureur, temps, 
    - Comparaison
 - OrderedLinkedList : une implémentation générale d'une liste chaînée ordonnée
    - __head, __length 
    - méthode accesseurs (first, size)
    - insert(resultat) - add(resultat) : ajouter un élément en respectant l'ordre croissant 
    - remove(coureur) : enlève le meilleur score d'un coureur (cette méthode n'est pas généralisable aux listes chaînées avec n'importe quel type de cargo, 
    puisqu'elle utilise explicitement l'attribut d'instance 'coureur' de Résultat, qui est le type de nos éléments de la liste)
    - search(coureur) : renvoie un tuple (resultat, position) (position commence à 1). même souci que pour remove quand à la dépendance à la classe Resultat.
    - get_as_array : transforme la liste chaînée en liste native python. Utile pour les tests et la méthode __str__
 - Classement : basé sur OrderedLinkedList. Taille limitée à 100 résultats.
    - méthodes accesseurs (size, result)
    - get(coureur) : retourne le résultat d'un coureur (basée sur search)
    - get_position(coureur) : retourne la position d'un coureur (basée sur search)
    - remove : basée sur remove


Deux classes de test sont implémentées avec 4 méthodes testées à chaque fois : 

 - OrderedLinkedListTest : init, add, remove, search
 - ClassementTest : add, get, remove, get_position

 Les étapes de chaque méthode de test sont similaires : 
 # init = initialisation supplémentaire
 # application = faire tourner la fonction à tester
 # comportement attendu = vérifier que tout est comme voulu
 # valeur par défaut = test des valeurs par défaut, car rien trouvé (ex : -1, False, None)