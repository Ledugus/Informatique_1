import search

filename = input("Spécifiez le nom de fichier: ")
index = search.create_index(filename)
while True:
    words = input("Spécifiez les mots a rechercher, en utilisant des espaces entre les mots: ")
    lines = search.get_lines(words.strip().split(), index)
    if not lines:
        print("Aucune ligne ne contient tous les mots. ")
    else:
        print("Les lignes suivantes contiennent tous les mots: ")
        for line in lines:
            print(line, end=" ")
            print()
