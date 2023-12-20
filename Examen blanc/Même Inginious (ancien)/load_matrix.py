def load_matrix(filename):
    # ce try catch toutes les exceptions sans distinctions
    try:
        f = open(filename, "r")
        # récupérer les dimensions
        lignes = int(f.readline().strip())
        colonnes = int(f.readline().strip())
        # créer la matrice vide
        matrix = [[0.0]*colonnes for _ in range(lignes)]
        # modifier la matrice pour chaque ligne suivante du fichier
        for line in f.readlines():
            raw_index, raw_value = line.strip().split()
            x, y = map(int, raw_index.split(","))
            value = int(raw_value)
            matrix[x][y] = value
        f.close()
        return matrix
    except:
        return -1
