import unittest
from translator import english_To_French, french_To_English

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_To_English('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_To_French('Hello'),'Bonjour')

unittest.main()