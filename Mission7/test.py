import search

def test_readfile():
    filename = "text_exemple_2.txt"
    list_result = ["the the the i must be", "the must be ...e allright()')\"' !!"]
    assert search.readfile(filename) == list_result, "Test 1 readfile échoué"
    print("Test readfile OK")

def test_get_words():
    string = "Turmoil has engulfed the Galactic Republic. They've won"
    list_result = ["turmoil", "has", "engulfed", "the", "galactic", "republic", "theyve", "won"]
    assert search.get_words(string) == list_result, "Test 1 get_words échoué"
    print("Test get_words OK")


def test_create_index():
    filename_1 = "text_exemple_1.txt"
    index_result_1 = {'for': [0], 'il': [1], 'deux': [1], 'course': [2], 'chance': [3], 'sil': [4]}
    filename_2 = "text_exemple_2.txt"
    index_result_2 = {'the': [0, 1], 'i': [0], 'must': [0, 1], 'be': [0, 1], 'e': [1], 'allright': [1]}
    assert search.create_index(filename_1) == index_result_1, "Test 1 create_index échoué"
    assert search.create_index(filename_2) == index_result_2, "Test 2 create_index échoué"
    print("Tests create_index OK")


def test_get_lines():
    index = {'for': [0, 1], 'il': [0, 2], 'deux': [0, 32], 'course': [0, 3], 'chance': [0, 1, 2, 32, 43]}
    words_1 = ["for", "il"]
    result_1 = [0]
    words_2 = ["deux", "chance"]
    result_2 = [0, 32]
    assert search.get_lines(words_1, index) == result_1, "Test 1 get_lines échoué"
    assert search.get_lines(words_2, index) == result_2, "Test 2 get_lines échoué"
    print("Tests get_lines OK")


test_readfile()
test_get_words()
test_get_lines()
test_create_index()
