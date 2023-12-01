import unittest

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [[] for row in range(numRows)]
    index = 0
    step = -1
    for char in s:
        rows[index].append(char)
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    for i in range(numRows):
        rows[i] = ''.join(rows[i])
    
    return ''.join(rows)

class convertTest(unittest.TestCase):
    def test_convert_case1(self, s="PAYPALISHIRING", numRows=3, solution="PAHNAPLSIIGYIR"):
        output = convert(s, numRows)
        self.assertEqual(output, solution)

    def test_convert_case2(self, s="PAYPALISHIRING", numRows=4, solution="PINALSIGYAHRPI"):
        output = convert(s, numRows)
        self.assertEqual(output, solution)

    def test_convert_case3(self, s="A", numRows=1, solution="A"):
        output = convert(s, numRows)
        self.assertEqual(output, solution)

if __name__ == "__main__":
    unittest.main()