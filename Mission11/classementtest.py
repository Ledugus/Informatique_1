import unittest
from classement import Classement
from coureur import Coureur
from resultat import Resultat
from temps import Temps


import unittest
from classement import Classement
from coureur import Coureur
from resultat import Resultat
from temps import Temps


class ClassementTest(unittest.TestCase):
    def setUp(self) -> None:
        self.coureurs = [Coureur("Alfred", 24),
                         Coureur("Bernard", 27),
                         Coureur("Claude", 19),
                         Coureur("François", 104)]

        self.temps = [Temps(1),
                      Temps(2),
                      Temps(3),
                      Temps(6)]

        self.results = [Resultat(self.coureurs[i], self.temps[i])
                        for i in range(4)]
        self.classement = Classement()

    def test_add(self):
        # application
        self.classement.add(self.results[0])
        # comportement attendu
        self.assertEqual(self.classement.get_position(self.coureurs[0]), 1)
        self.assertEqual(self.classement.size(), 1)
        # application
        self.classement.add(self.results[1])
        # comportement attendu
        self.assertEqual(self.classement.get(
            self.coureurs[1]), self.results[1])
        self.assertEqual(self.classement.get_position(self.coureurs[1]), 2)
        # application
        self.classement.add(self.results[2])
        # comportement attendu
        self.assertEqual(self.classement.get_position(self.coureurs[2]), 3)
        self.assertEqual(self.classement.get_position(self.coureurs[1]), 2)
        self.assertEqual(self.classement.size(), 3)

    def test_get(self):
        # application
        self.classement.add(self.results[1])
        # comportement attendu
        self.assertEqual(
            self.results[1], self.classement.get(self.coureurs[1]))
        # valeur par défaut
        self.assertEqual(
            None, self.classement.get(self.coureurs[2]))

    def test_remove(self):
        # init
        self.test_add()
        # application
        self.classement.remove(self.results[1].coureur())
        # comportement attendu
        self.assertEqual([self.results[0], self.results[2]],
                         self.classement.result().get_as_array())
        # valeur par défaut
        self.assertFalse(self.classement.remove(self.coureurs[1]))

    def test_get_position(self):
        # init
        self.classement.add(self.results[3])
        # comportement attendu
        self.assertEqual(1, self.classement.get_position(self.coureurs[3]))
        # valeur par défaut
        self.assertEqual(-1, self.classement.get_position(self.coureurs[1]))


if __name__ == "__main__":
    unittest.main()
