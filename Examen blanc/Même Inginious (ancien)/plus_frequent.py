def plus_frequent(l: list):
    current_max = l[0]
    max_count = 1
    for ele in l:
        current_count = l.count(ele)
        if current_count > max_count:
            current_max = ele
            max_count = current_count
    return current_max


# test de la fonction plus_frequent -> sortie = b
print(plus_frequent(["aa", "aa", "b", 3, ["b"]*10,
      {"b", "b", "b", "b"}, 0, 0, 3, 7, "b", "b", "bbbbbb"]))
