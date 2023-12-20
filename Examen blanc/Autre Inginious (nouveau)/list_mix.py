def mix(l: list):
    r = []
    for x in range(len(l)//2):
        # ajouter l'élément actuel
        r.append(l[x])
        # ajouter son symétrique
        r.append(l[len(l)-x-1])
    return r


print(mix([1, 2, 3, 4, "A", "B"]))
