import unittest


def find_missing(seq):
    for i, item in enumerate(seq[:-2]):
        if (seq[i] + seq[i+2]) / 2 == seq[i+1]:
            continue
        diff = seq[i+1] - seq[i]
        result = seq[i+1] + diff
        if result > seq[-1] or result in seq:
            diff = seq[i+2] - seq[i+1]
            result = seq[i+1] - diff
        return result 


class ArithmeticProgressionTest(unittest.TestCase):
    def test_short_case(self):
        array = [1, 2, 4]
        self.assertEqual(find_missing(array), 3)
        array = [1, 3, 4]
        self.assertEqual(find_missing(array), 2)

    def test_long_case(self):
        array = [1, 3, 5, 9, 11]
        self.assertEqual(find_missing(array), 7)
        array = [1, 2, 3, 4, 6, 7, 8, 9]
        self.assertEqual(find_missing(array), 5)

    def test_three_diff(self):
        array = [1, 7, 10, 13]
        self.assertEqual(find_missing(array), 4)
        array = [1, 4, 10, 13]
        self.assertEqual(find_missing(array), 7)
        array = [1, 4, 7, 10, 16]
        self.assertEqual(find_missing(array), 13)



def main():
    unittest.main()

if __name__ == '__main__':
    main()