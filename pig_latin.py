import unittest

def pig_it(text):
    new_text = ''
    for word in text.split():
        if word.isalnum():
            word = word[1:] + word[0] + 'ay'
        new_text += word + " "
    new_text = new_text[:-1]
    return new_text

class PigLatinTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_one(self):
        latin = pig_it('Pig latin is cool')
        expected = 'igPay atinlay siay oolcay'
        self.assertEqual(latin, expected)

    def test_two(self):
        latin = pig_it('This is my string')
        expected = 'hisTay siay ymay tringsay'
        self.assertEqual(latin, expected)

    def test_three(self):
        latin = pig_it('This is my string ?')
        expected = 'hisTay siay ymay tringsay ?'
        self.assertEqual(latin, expected)

def main():
    unittest.main()

if __name__ == '__main__':
    main()