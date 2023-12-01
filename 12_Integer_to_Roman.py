import unittest

def intToRoman(num: int) -> str:
        int_roman_dict = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }

        res = ''
        for key, val in int_roman_dict.items():
            while key <= num :
                res += val * (num//key)
                num -= (num//key) * key

        return res

class intToRomanTest(unittest.TestCase):
    def test_intToRoman_case1(self, num=3, solution="III"):
        output = intToRoman(num)
        self.assertEqual(output, solution)

    def test_intToRoman_case2(self, num=58, solution="LVIII"):
        output = intToRoman(num)
        self.assertEqual(output, solution)

    def test_intToRoman_case3(self, num=1994, solution="MCMXCIV"):
        output = intToRoman(num)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()