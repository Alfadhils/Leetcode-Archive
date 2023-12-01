import unittest

def romanToInt(s: str) -> int:
    roman_to_int = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    total = 0
    for i, char in enumerate(s):
        if i != len(s)-1 and roman_to_int[char]<roman_to_int[s[i+1]]:
            total += -roman_to_int[char]
        else :
            total += roman_to_int[char]
    
    return total

class romanToIntTest(unittest.TestCase):
    def test_romanToInt_case1(self, s="III", solution=3):
        output = romanToInt(s)
        self.assertEqual(output, solution)

    def test_romanToInt_case2(self, s="LVIII", solution=58):
        output = romanToInt(s)
        self.assertEqual(output, solution)

    def test_romanToInt_case3(self, s="MCMXCIV", solution=1994):
        output = romanToInt(s)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()