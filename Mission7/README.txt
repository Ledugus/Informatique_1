Augustin Wezel, 7/11/2023

Ce programme lit, indexe et permet la recherche de mots dans un fichier.

Le programme considère tout fichier non trouvé comme un fichier vide et s'exÃ©cute sans exception. Il ne trouvera donc pas d'index à retourner.

Le fichier "test.py" teste les fonctions suivantes de "search.py" :
    readfile(filename),
    get_words(line),
    create_index(filename),
    get_lines(words, index)

selon les fichiers tests "text_exemple_1.txt" et "text_exemple_2.txt".