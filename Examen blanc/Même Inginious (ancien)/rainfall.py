def rainfall(liste: list[int]) -> float:
    # éliminer les nombres > 9999 et max(0, x) met les nombres négatif à 0
    new_list = [max(0, x) for x in liste if x < 9999]
    # retourner la moyenne
    return sum(new_list)/len(new_list)


print(rainfall([1, -3, 20, 10000]))
