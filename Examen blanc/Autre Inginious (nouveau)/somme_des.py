def somme_des(n):
    d = {}
    for val1 in range(1, n+1):
        for val2 in range(1, n+1):
            d[val1+val2] = d.get(val1+val2, [])
            d[val1+val2].append((val1, val2))

    return d


print(somme_des(6))
