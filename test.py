import unittest
import mainscript

class Test(unittest.TestCase):

    def test_tempEqual(self):
        result = mainscript.temperatureConverter(98.6,1)
        self.assertEqual(result,37.0)

    def test_tempNotEqual(self):
        result = mainscript.temperatureConverter(37,2)
        self.assertNotEqual(result,99)

    def test_vowelsTrue(self):
        result = mainscript.Vowels("clouds")
        self.assertTrue(result)

    def test_vowelsFalse(self):
        result = mainscript.Vowels("sky")
        self.assertFalse(result)

    def test_forceGreater(self):
        result = mainscript.Force(50)
        self.assertGreater(result,60)

    def test_forceLesser(self):
        result = mainscript.Force(5)
        self.assertLess(result,60)
    
if __name__ == '__main__':
	unittest.main()
