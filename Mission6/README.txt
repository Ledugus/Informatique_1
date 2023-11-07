Voici le tout nouveau assistant Pythonicus !
Il peut vous aider lors de votre recherche de mots en anglais et pour quelques opérations mathématiques de la vie de tous les jours.

Commandes possibles :
file <name>: spécifier le nom d'un fichier sur lequel travailler
info: montrer le nombre de lignes et de caractères du fichier
words: utiliser le fichier comme liste de mots
search <word>: déterminer si le mot est dans la liste de mots
sum <number1> ... <numbern>: calculer la somme des nombres spécifiés
avg <number1> ... <numbern>: calculer la moyenne des nombres spécifiés
help: liste des commandes possibles
exit: arrêter l'assistant

Fonctionnement du programme :
- Une boucle while qui demande les commandes à l'utilisateur
- Une fonction exécute qui appelle la fonction correspondant à la commande selon le dictionnaire COMMANDS
- Chaque fonction accomplit les actions demandées, imprime les résultat et gère les exceptions de manière autonome
- Il y a un gestionnaire d'erreurs "print_error" qui imprime les erreurs selon le message spécifié (possibilité d'ajouter un format d'erreur global facilement)
- Variables globales pour enregistrer l'état du programme