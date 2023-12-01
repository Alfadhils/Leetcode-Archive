import unittest

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
        if char in magazine :
            magazine = magazine.replace(char,'',1)
        else :
            return False
    return True

class canConstructTest(unittest.TestCase):
    def test_canConstruct_case1(self, ransomNote="a", magazine="b", solution=False):
        output = canConstruct(ransomNote, magazine)
        self.assertEqual(output, solution)

    def test_canConstruct_case2(self, ransomNote="aa", magazine="ab", solution=False):
        output = canConstruct(ransomNote, magazine)
        self.assertEqual(output, solution)

    def test_canConstruct_case3(self, ransomNote="aa", magazine="aab", solution=True):
        output = canConstruct(ransomNote, magazine)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()