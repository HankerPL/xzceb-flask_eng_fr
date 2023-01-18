import unittest
from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase): 
    """UNIT test 1 - english_to_french TEST"""
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Hello World'), 'Bonjour le monde')
        self.assertNotEqual(english_to_french('Advanced Python'), 'Python simple')
        self.assertAlmostEqual(english_to_french('advanced'), 'avance')
        

class test_french_to_english(unittest.TestCase): 
    """UNIT test 2 - frenchToEnglish TEST"""
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bonjour le monde'), 'Hello World')
        self.assertNotEqual(french_to_english('Python simple'), 'Advanced Python')
        self.assertAlmostEqual(french_to_english('avance'), 'advanced')

unittest.main()
