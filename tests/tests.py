import unittest

from machinetranslation.translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english_null_input(self):
        self.assertNotEqual(french_to_english('Bonjour'),None)
        
    def test_english_to_french_null_input(self):
        self.assertNotEqual(english_to_french('Hello'),None)
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        
if __name__ == '__main__':
    unittest.main()