# 1160. Find Words That Can Be Formed by Characters

## Intuition
The problem requires counting the total length of words in a given list that can be formed using the characters in another string. The idea is to iterate through each word in the list and check if it can be formed using the characters in the given string.

## Approach
The approach used here is a straightforward one. For each word in the list, iterate through its characters. Check if each character is present in the given string. If a character is found, remove it from the string, indicating that it has been used. If a character is not found, set a flag `valid` to 0, indicating that the current word cannot be formed. At the end of each word iteration, if the `valid` flag is still 1, add the length of the word to the result.

## Complexity
- Time complexity: O(n * m), where n is the number of words in the list and m is the average length of the words. The nested loop goes through each character in each word.
- Space complexity: O(m), where m is the length of the given string `chars`. The space is used to create a list of characters from the string.

## Code
```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            valid = 1
            base = list(chars)
            for char in word:
                if char not in base:
                    valid = 0
                    break
                else:
                    base.remove(char)
            
            if valid:
                res += len(word)
            
        return res
