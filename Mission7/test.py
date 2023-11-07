import search


def test_get_words():
    string = "Turmoil has engulfed the Galactic Republic. They've won"
    list_result = ["turmoil", "has", "engulfed", "the", "galactic", "republic", "theyve", "won"]
    assert search.get_words(string) == list_result, "Test 1 get_words échoué"
    print("Test get_words OK")


def test_create_index():
    filename = "text_exemple_1.txt"
    index_result = {'for': [1], 'il': [2], 'deux': [2], 'course': [3], 'chance': [4], 'sil': [5]}
    assert search.create_index(filename) == index_result, "Test 1 create_index échoué"
    print("Test create_index OK")


def test_get_lines():
    index = {'for': [0, 1], 'il': [0, 2], 'deux': [0, 32], 'course': [0, 3], 'chance': [0, 1, 2, 32, 43]}
    words_1 = ["for", "il"]
    result_1 = [0]
    words_2 = ["deux", "chance"]
    result_2 = [0, 32]
    assert search.get_lines(words_1, index) == result_1, "Test 1 get_lines échoué"
    assert search.get_lines(words_2, index) == result_2, "Test 2 get_lines échoué"
    print("Test get_lines OK")


test_get_words()
test_get_lines()
test_create_index()
