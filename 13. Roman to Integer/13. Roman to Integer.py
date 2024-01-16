class Solution:
    def romanToInt(self, s: str) -> int:
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