import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(''),'Text should not be empty') #null input
        self.assertEqual(englishToFrench('Hello'),'Bonjour') #Hello input -> Bonjour output
        
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(''),'Text should not be empty') #null input
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") #Bonjour input -> Hello output
        
unittest.main()
