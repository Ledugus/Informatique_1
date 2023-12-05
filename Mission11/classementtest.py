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
                         Coureur("Claude", 19)]

        self.temps1 = Temps(1)
        self.temps2 = Temps(2)
        self.temps3 = Temps(3)
        self.temps4 = Temps(6)

        self.result1 = Resultat(self.coureurs[0], self.temps1)
        self.result2 = Resultat(self.coureurs[1], self.temps2)
        self.result3 = Resultat(self.coureurs[2], self.temps3)

        self.classement = Classement()

    def test_add(self):
        self.classement.add(self.result1)
        self.assertEqual(self.classement.get_position(self.coureurs[0]), 1)

        self.classement.add(self.result2)
        self.assertEqual(self.classement.get(self.coureurs[1]), self.result2)
        self.assertEqual(self.classement.get_position(self.coureurs[1]), 2)
        self.classement.add(self.result3)
        self.assertEqual(self.classement.get_position(self.coureurs[2]), 3)

    def test_get(self):
        self.classement.add(self.result2)
        self.assertEqual(self.result2, self.classement.get(self.coureurs[1]))
        self.classement.remove(self.coureurs[1])

    def test_remove(self):
        self.test_add()
        self.classement.remove(self.result2.coureur())
        self.assertEqual([self.result1, self.result3],
                         self.classement.result().get_as_array())


if __name__ == "__main__":
    unittest.main()
